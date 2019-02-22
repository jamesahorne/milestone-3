import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'milestone_4'
app.config['MONGO_URI'] = 'mongodb://#username#:#password#@ds251827.mlab.com:51827/milestone_4'


# app.config['MONGO_URI'] = os.getenv('MONGO_URI')   #   ! ! !   FIX THIS   ! ! !


mongo = PyMongo(app)


#recipes = mongo.db.recipes - would this work?


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html', 
                            recipes=mongo.db.recipes.find())

@app.route('/full_recipe/<recipe_id>')
def full_recipe(recipe_id):
    return render_template('full_recipe.html',
                            recipes=mongo.db.recipes.find(),
                            ingredients=mongo.db.ingredients.find(),
                            portion_sizes=mongo.db.portion_sizes.find(),
                            total_times=mongo.db.total_times.find(),
                            allergens=mongo.db.allergens.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
                            ingredients=list(mongo.db.ingredients.find()),
                            portion_sizes=mongo.db.portion_sizes.find(),
                            total_times=mongo.db.total_times.find(),
                            allergens=mongo.db.allergens.find())

@app.route('/add_ingredient')
def add_ingredient():
    return render_template('add_ingredient.html')

@app.route('/add_allergen')
def add_allergen():
    return render_template('add_allergen.html')


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))

@app.route('/insert_ingredient', methods=['POST'])
def insert_ingredient():
    ingredients = mongo.db.ingredients
    ingredients.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))

@app.route('/insert_allergen', methods=['POST'])
def insert_allergen():
    allergens = mongo.db.allergens
    allergens.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html',
                            recipes=the_recipe,
                            ingredients=list(mongo.db.ingredients.find()),
                            portion_sizes=mongo.db.portion_sizes.find(), 
                            total_times=mongo.db.total_times.find(),
                            allergens=mongo.db.allergens.find())

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'username':request.form.get('username'),
        'description':request.form.get('description'),
        'main_ingredient':request.form.get('main_ingredient'),
        'vegetarian':request.form.get('vegetarian'),
        'serves':request.form.get('serves'),
        'total_time':request.form.get('total_time'),
        'ingredient_name':request.form.get('ingredient_name'),
        'allergens':request.form.get('allergens'),
        'method':request.form.get('method'),
    })
    return redirect(url_for('recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes'))


@app.route('/data')
def data():
    return render_template('data.html', recipes=mongo.db.recipes.find())
  

@app.route('/get_data')
def get_data():
    keys = {'main_ingredient': True, '_id': False}
  
    recipes = dumps(mongo.db.recipes.find(projection=keys))
  
    return recipes


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
