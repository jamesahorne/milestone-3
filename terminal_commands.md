// Install Flask on Python3
sudo pip3 install flask

// Connect Cloud9 to Heroku by logging in
heroku login
 - enter email and password

// On the Heroku website (in my "milestone-4" app, in the Deploy section) I've connected my Heroku account to my "milestone_4" GitHub repo, meaning when I commit to Heroku, Heroku automatically pushes the commit to my GitHub repo (instead of me having to commit to both).

// Add requirements.txt file
sudo pip3 freeze --local > requirements.txt

// Add Procfile
echo web: python app.py > Procfile

// Initialise a Git repo
git init

// Add all untracked files
git commit -m "Initial commit"

// Make the "milestone-4" Heroku app the remote master branch
heroku git:remote -a milestone-4

// Push to Heroku
git push heroku master

// Scale dynos
heroku ps:scale web=1

// Install Flask-PyMongo - similar to PyMongo but optimised to work with Flask
sudo pip3 install flask_pymongo

// Set MONGO_URI environment variable in a secure way
export MONGO_URI=mongodb://#username#:#password#@ds251827.mlab.com:51827/milestone_4
