import os
from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'milestone_4'
app.config['MONGO_URI'] = 'mongodb://#username#:#password#@ds251827.mlab.com:51827/milestone_4'


# app.config['MONGO_URI'] = os.getenv('MONGO_URI') -   ! ! !   FIX THIS   ! ! !


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
