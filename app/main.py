import os, flask
from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from .utils import files

ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
db = SQLAlchemy(app)

app.config["IMAGE_UPLOADS"] = ROOT + "/static/assets/images"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024


@app.before_first_request
def create_tables():
    db.create_all()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imageLink = db.Column(db.String(50), nullable=True, default="No Provided Image")
    plantName = db.Column(db.String(30), nullable=True, default="Unknown Plant")
    title = db.Column(db.String(100), nullable=True, default=("Post number" + id))
    description = db.Column(db.Text, nullable=True, default="No Description Provided")
    author = db.Column(db.String(30), nullable=True, default='Anonymous')
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return 'Post ' + str(self.id)


def commitPost(request, image_link=""):
    plant_Name =      request.form.get('plantName', False)
    post_title =      request.form.get('title', False)
    post_content =    request.form.get('description', False)
    post_author = request.form.get('author', False)
    new_post = Post(title=post_title, description=post_content, plantName=plant_Name, imageLink=image_link, author=post_author)
    db.session.add(new_post)
    db.session.commit()

@app.route('/newpost', methods=['GET', 'POST'])
def newPost():
    if request.method == 'POST':
        if request.files:
            image = request.files["image"]
            
            if "filesize" in request.cookies:
                if not files.allowed_image_filesize(app, request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

            if files.allowed_image(app, image.filename):
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
                image_link = image.filename

        commitPost(request, image_link)
        return redirect('/allposts')
    elif request.method == 'GET':
        all_posts = Post.query.order_by(Post.date_posted).all()
        return render_template('newpost.html', posts=all_posts)


@app.route('/allposts', methods=['GET'])
def allPosts():
    all_posts = Post.query.order_by(Post.date_posted).all()
    return render_template('allPosts.html', posts=all_posts)

@app.route('/maps', methods=['GET'])
def maps():
    all_posts = Post.query.order_by(Post.date_posted).all()
    return render_template('maps.html', posts=all_posts)

@app.route("/")
def index():
    return flask.render_template('index.html')