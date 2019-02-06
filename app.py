import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'milestone_4'
app.config['MONGO_URI'] = 'mongodb://#username#:#password#@ds251827.mlab.com:51827/milestone_4'


# app.config['MONGO_URI'] = os.getenv('MONGO_URI')   #   ! ! !   FIX THIS   ! ! !


mongo = PyMongo(app)

#recipes = mongo.db.recipes - would this work?

@app.route('/')

@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', 
                            recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
                            ingredients=mongo.db.ingredients.find(), 
                            allergens=mongo.db.allergens.find())

@app.route('/insert_recipe')
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.toDict())
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
