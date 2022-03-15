import os
from flask import Flask
import flask

# template_dir = os.path.dirname(os.path.abspath(__file__))
# app = Flask(__name__, template_folder=template_dir)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template('index.html')