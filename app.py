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

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           categories=mongo.db.categories.find(), utensils=mongo.db.utensils.find())

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))

@app.route('/manage_recipes/')
def manage_recipes():
    return render_template('manage_recipes.html', manage_recipes=mongo.db.recipes.find())

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('manage_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html',
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name')
    })
    return redirect(url_for('manage_recipes'))

@app.route('/view_categories/')
def view_categories():
    return render_template('view_categories.html', view_categories=mongo.db.categories.find())

@app.route('/insert_category', methods=["POST"])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    category_doc = {'category_image': request.form.get('category_image')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('view_categories'))

@app.route('/add_category/')
def add_category():
    return render_template('add_category.html')

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('edit_category.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))

@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    category = mongo.db.categories
    category.update( {'_id': ObjectId(category_id)},
    {
        'category_name': request.form.get('category_name'),
        'category_image': request.form.get('category_image')
    })
    return redirect(url_for('view_categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('manage_categories'))

@app.route('/manage_categories/')
def manage_categories():
    return render_template('manage_categories.html', manage_categories=mongo.db.categories.find())






if __name__ == '__main__':
    app.run(host='0.0.0.0',

            port=(os.environ.get('PORT')),
            debug=True)