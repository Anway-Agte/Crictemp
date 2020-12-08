from flask import (
    Flask,
    render_template,
    session,
    redirect,
    request,
    url_for,
    flash,
    Response,
    make_response,
    Markup,
)
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/cricblog"
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/')
def home():
   return(render_template('index.html'))

if __name__ == "__main__":
    app.run(debug=True)