import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'milestone_4'
app.config['MONGO_URI'] = 'mongodb://#:#@ds251827.mlab.com:51827/milestone_4'


# app.config['MONGO_URI'] = os.getenv('MONGO_URI')   #   ! ! !   FIX THIS   ! ! !


#        Variables        #


mongo = PyMongo(app)
recipes = mongo.db.recipes
vegetarian = mongo.db.vegetarian.find(),
ingredients = mongo.db.ingredients.find()
portion_sizes = mongo.db.portion_sizes.find()
total_times = mongo.db.total_times.find()
allergens=mongo.db.allergens.find()


#        Home & recipes        #


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recipes')
def get_recipes():
    return render_template('recipes.html', 
                            recipes=recipes.find())


@app.route('/full_recipe/<recipe_id>')
def full_recipe(recipe_id):
    the_recipe =  recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('full_recipe.html',
                            recipe=the_recipe)


#        Add        #


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                            vegetarian=vegetarian,
                            ingredients=list(ingredients.find()),
                            portion_sizes=portion_sizes,
                            total_times=total_times,
                            allergens=allergens.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes.insert_one({
        'recipe_name':request.form.get('recipe_name'),
        'username':request.form.get('username'),
        'description':request.form.get('description'),
        'main_ingredient':request.form.get('main_ingredient'),
        'vegetarian':request.form.get('vegetarian'),
        'serves':request.form.get('serves'),
        'time':request.form.get('time'),
        'allergens':request.form.getlist('allergens'),
        'ingredients':request.form.getlist('ingredients'),
        'method':request.form.get('method')
    })
    return redirect(url_for('recipes'))


@app.route('/add_ingredient')
def add_ingredient():
    return render_template('add_ingredient.html')


@app.route('/insert_ingredient', methods=['POST'])
def insert_ingredient():
    ingredients.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))


@app.route('/add_allergen')
def add_allergen():
    return render_template('add_allergen.html')


@app.route('/insert_allergen', methods=['POST'])
def insert_allergen():
    allergens.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))


#        Edit & delete        #


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html',
                            recipes=the_recipe,
                            vegetarian=vegetarian,
                            ingredients=list(ingredients.find()),
                            portion_sizes=portion_sizes, 
                            total_times=total_times,
                            allergens=allergens.find())


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'username':request.form.get('username'),
        'description':request.form.get('description'),
        'main_ingredient':request.form.get('main_ingredient'),
        'vegetarian':request.form.get('vegetarian'),
        'serves':request.form.get('serves'),
        'time':request.form.get('time'),
        'allergens':request.form.getlist('allergens'),
        'ingredients':request.form.getlist('ingredients'),
        'method':request.form.get('method')
    })
    return redirect(url_for('recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes'))


#        Data        #


@app.route('/data')
def data():
    recipe_count = recipes.count()
    
    return render_template('data.html',
                            recipes=recipes.find(),
                            recipe_count=recipe_count)


@app.route('/get_data')
def get_data():
    keys = {'main_ingredient': True, 'allergens': True, 'vegetarian': True, 'time': True, '_id': False}
  
    recipe_keys = dumps(recipes.find(projection=keys))
  
    return recipe_keys


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
