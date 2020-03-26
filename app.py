import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

from os import path 
if path.exists("env.py"):
    import env

app = Flask(__name__)

from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app.config["MONGO_DBNAME"] = 'windy-millers_bakery'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

from flask import Flask, render_template, redirect, request, url_for

@app.route('/')
@app.route('/recipes')
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes )
    
@app.route('/categories/')
def categories():
    return render_template('categories.html', categories=mongo.db.categories.find())

@app.route('/insert_category', methods=["POST"])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('categories'))

@app.route('/add_category/')
def add_category():
    return render_template('add_category.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',

            port=(os.environ.get('PORT')),
            debug=True)