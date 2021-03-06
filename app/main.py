import os, flask
import re, base64
from datetime import datetime
from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from .utils import files

ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
db = SQLAlchemy(app)
maps_api_key = os.environ.get('MAPS')


# debug mode on
app.debug = True

app.config["IMAGE_UPLOADS"] = ROOT + "/static/assets/images"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# if maps_api_key is not None:
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.environ.get('URI'))
print(app.config['SQLALCHEMY_DATABASE_URI'])


@app.before_first_request
def create_tables():
    # create tables if they don't exist
    db.create_all()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plantName = db.Column(db.String(30), nullable=True, default="Unknown Plant")
    title = db.Column(db.String(100), nullable=True, default=("Post number" + id))
    description = db.Column(db.Text, nullable=True, default="No Description Provided")
    location = db.Column(db.String(30), nullable=True, default='No Location Given')
    image = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.String(30), nullable=True, default="Unknown Image")

    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Post ' + str(self.id)

def commitPost(request, image):
    plant_Name =      request.form.get('plantName', False)
    post_title =      request.form.get('title', False)
    post_content =    request.form.get('description', False)
    location = request.form.get('location', False)
    mimetype = image.mimetype
    print(mimetype)
    image = image.read()

    new_post = (
    Post(title=post_title, 
     description=post_content, 
     plantName=plant_Name, 
     location=location, 
     image=base64.b64encode(image).decode('utf-8'),
     mimetype=mimetype)
    )
    db.session.add(new_post)
    db.session.commit()

@app.route('/newpost', methods=['GET', 'POST'])
def newPost():
    if request.method == 'POST':
        if request.files:
            image = request.files["image"]
            
            # if "filesize" in request.cookies:
            #     if not files.allowed_image_filesize(app, request.cookies["filesize"]):
            #         print("Filesize exceeded maximum limit")
            #         return redirect(request.url)

            # if files.allowed_image(app, image.filename):
            #     # image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            #     image_link = image.filename

            commitPost(request, image)

        return redirect('/allposts')
    elif request.method == 'GET':
        all_posts = Post.query.order_by(Post.date_posted).all()
        return render_template('newpost.html', posts=all_posts)


@app.route('/allposts', methods=['GET'])
def allPosts():
    # all_posts = Post.query.order_by(Post.date_posted).all()
    all_posts = db.session.query(Post).all()

    return render_template('allPosts.html', posts=all_posts)

@app.route('/maps', methods=['GET'])
def maps():
    # all_posts = Post.query.order_by(Post.date_posted).all()
    all_posts = db.session.query(Post).all()

    print("All posts = ", *all_posts)
    return render_template('maps.html', posts=all_posts, api=maps_api_key)

@app.route('/timeline', methods=['GET'])
def timeline():
    return render_template("timeline.html")

@app.route('/resources', methods=['GET'])
def resources():
    return render_template("resources.html")

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route('/allposts/delete/<int:id>')
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/allposts')