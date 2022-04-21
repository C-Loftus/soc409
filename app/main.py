import os, flask
import re, base64
from datetime import datetime
from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import io

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

class Evaluation(db.Model) : 
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Text, nullable=True, default=(""))
    q2 = db.Column(db.Text, nullable=True, default=(""))
    # q3 = db.Column(db.String(100), nullable=True, default=(""))
    # q4 = db.Column(db.Text, nullable=True, default=(""))

    # date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Evaluation ' + str(self.id)

def commitEvaluation(request) : 

    q1 = request.form.get('q1', False)
    q2 = request.form.get('q2', False)
    q3 = request.form.get('q3', False)
    # q4 = request.form.get('q4', False)
    new_evaluation = (
        Evaluation(q1=q1, q2=q2)
    )
    db.session.add(new_evaluation)
    db.session.commit()

@app.route('/evaluation', methods=['GET', 'POST'])
def newEvaluation() : 
    if request.method == 'POST':
        commitEvaluation(request)
        return redirect('/wordcloud')
    elif request.method == 'GET':
        print("IN GET")
        # all_posts = Post.query.order_by(Post.date_posted).all()
        return render_template('evaluation.html')

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

@app.route('/wordcloud', methods=['GET'])
def wordCloudGenerator():
    # all_evals = db.session.query(Evaluation).all()
    # for eval in all_evals : 
    #     id = eval.id
    #     to_delete = Evaluation.query.get_or_404(id)
    #     db.session.delete(to_delete)
    # db.session.commit()
    all_evals = db.session.query(Evaluation).all()
    words = []
    for eval in all_evals : 
        words += eval.q1.split(" ")
        words += eval.q2.split(" ")
    words = " ".join(words)
    if len(words) == 0 : 
        print("No evaluations yet")
        return render_template("evaluation.html")
    wordcloud = WordCloud(width = 800, height = 500,
                    background_color ='black',
                    min_font_size = 10).generate(words)
    
    wordcloud.to_file("wordcloud.png")

    im = Image.open("wordcloud.png")
    data = io.BytesIO()
    im.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return render_template("wordcloud.html", img_data=encoded_img_data.decode('utf-8'))

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route('/allposts/delete/<int:id>')
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/allposts')