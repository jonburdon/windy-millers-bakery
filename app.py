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
    categories=mongo.db.categories.find()
    utensils=mongo.db.utensils.find()
    utensils2=mongo.db.utensils.find()
    utensil3=["one", "two", "three"]
    return render_template("recipes.html", recipes=recipes, categories=categories, utensils=utensils, utensils2=utensils2, 
    recipecount=mongo.db.recipes.count_documents({"published": { "$in": ["on"]}})
    , featuredrecipes=mongo.db.recipes.count_documents(
                    {"recipe_featured": { "$in": ["on"]}}
        )
    , recipecategories=mongo.db.categories.count_documents({"published": { "$in": ["on"]}})
    , utensilcount=mongo.db.utensils.count_documents({"published": { "$in": ["on"]}})
    )

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    i= 0
    all_recipes = mongo.db.recipes.find()
    for recipe in all_recipes:
        for r in recipe:
            print(r)
            #print(recipe.preparation_time)
            #if recipe.preparation_time <= 15:
            #    i+=1
            #print(recipe)
        print(i)
   
    
    return render_template('view_recipe.html',
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}), 
    recipecount=mongo.db.recipes.count_documents({"published": { "$in": ["on"]}})
    , featuredrecipes=mongo.db.recipes.count_documents(
                    {"recipe_featured": { "$in": ["on"]}}
        )
    , recipecategories=mongo.db.categories.count_documents({"published": { "$in": ["on"]}})
    ,
    quickrecipes=mongo.db.recipes.count_documents({"preparation_time": { "$lt": 15}})
    
    
    )
    

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
    return redirect(url_for('manage_archive'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html',
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}),
                           categories=mongo.db.categories.find(), utensils=mongo.db.utensils.find())

@app.route('/archive_recipe/<recipe_id>')
def archive_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.update_one(
   { "_id": ObjectId(recipe_id) },
   { "$set": { "published": "off" } }
)
    return redirect(url_for('manage_recipes'))

@app.route('/restore_recipe/<recipe_id>')
def restore_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.update_one(
   { "_id": ObjectId(recipe_id) },
   { "$set": { "published": "on" } }
)
    return redirect(url_for('manage_archive'))

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_serves': request.form.get('recipe_serves'),
        'utensil_list': request.form.get('utensil_list'),
        'ingredients_list': request.form.get('ingredients_list'),
        'method': request.form.get('method'),
        'preparation_time': request.form.get('preparation_time'),
        'cooking_time': request.form.get('cooking_time'),
        'tips': request.form.get('tips'),
        'photo_url': request.form.get('photo_url'),
        'category_name': request.form.get('category_name'),
        'featured_utensil': request.form.get('featured_utensil'),
        'published': request.form.get('published'),
        'recipe_featured': request.form.get('recipe_featured')
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
    return redirect(url_for('manage_archive'))

@app.route('/archive_category/<category_id>')
def archive_category(category_id):
    category = mongo.db.categories
    category.update_one(
   { "_id": ObjectId(category_id) },
   { "$set": { "published": "off" } }
)
    return redirect(url_for('manage_categories'))

@app.route('/restore_category/<category_id>')
def restore_category(category_id):
    category = mongo.db.categories
    category.update_one(
   { "_id": ObjectId(category_id) },
   { "$set": { "published": "on" } }
)
    return redirect(url_for('manage_archive'))

@app.route('/manage_categories/')
def manage_categories():
    return render_template('manage_categories.html', manage_categories=mongo.db.categories.find())

@app.route('/utensil/<utensil_id>')
def utensil(utensil_id):
    return render_template('view_utensil.html',
    utensil=mongo.db.utensils.find_one({'_id': ObjectId(utensil_id)}))

@app.route('/view_utensils/')
def view_utensils():
    return render_template('view_utensils.html', view_utensils=mongo.db.utensils.find())

@app.route('/manage_utensils/')
def manage_utensils():
    return render_template('manage_utensils.html', manage_utensils=mongo.db.utensils.find())

@app.route('/edit_utensil/<utensil_id>')
def edit_utensil(utensil_id):
    return render_template('edit_utensil.html',
    utensil=mongo.db.utensils.find_one({'_id': ObjectId(utensil_id)}))

@app.route('/delete_utensil/<utensil_id>')
def delete_utensil(utensil_id):
    mongo.db.utensils.remove({'_id': ObjectId(utensil_id)})
    return redirect(url_for('manage_archive'))

@app.route('/archive_utensil/<utensil_id>')
def archive_utensil(utensil_id):
    utensil = mongo.db.utensils
    utensil.update_one(
   { "_id": ObjectId(utensil_id) },
   { "$set": { "published": "off" } }
)
    return redirect(url_for('manage_utensils'))

@app.route('/restore_utensil/<utensil_id>')
def restore_utensil(utensil_id):
    utensil = mongo.db.utensils
    utensil.update_one(
   { "_id": ObjectId(utensil_id) },
   { "$set": { "published": "on" } }
)
    return redirect(url_for('manage_archive'))

@app.route('/add_utensil/')
def add_utensil():
    return render_template('add_utensil.html')

@app.route('/insert_utensil', methods=["POST"])
def insert_utensil():
    utensils = mongo.db.utensils
    utensils.insert_one(request.form.to_dict())
    return redirect(url_for('view_utensils'))

@app.route('/update_utensil/<utensil_id>', methods=['POST'])
def update_utensil(utensil_id):
    utensil = mongo.db.utensils
    utensil.update( {'_id': ObjectId(utensil_id)},
    {
        'utensil_name': request.form.get('utensil_name'),
        'published': request.form.get('published'),
        'utensil_description': request.form.get('utensil_description'),
        'image_url': request.form.get('image_url'),
        'delux_range': request.form.get('delux_range'),
        'shop_url': request.form.get('shop_url')
    })
    return redirect(url_for('manage_utensils'))

@app.route('/manage_archive/')
def manage_archive():
    return render_template('manage_archive.html', manage_categories=mongo.db.categories.find()
    , manage_utensils=mongo.db.utensils.find()
    , manage_recipes=mongo.db.recipes.find())

@app.route('/manage/')
def manage():
    return render_template('manage.html', manage_categories=mongo.db.categories.find()
    , manage_utensils=mongo.db.utensils.find()
    , manage_recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host='0.0.0.0',

            port=(os.environ.get('PORT')),
            debug=True)