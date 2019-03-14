# Subify (Sandwich Filling Recipe Site)
This project is for Milestone 3 of Code Institutes Full Stack Development Diploma, and uses Python, Flask and MongoDB in the backend and HTML, CSS, Materialize and JavaScript in the frontend.

[Subify](https://milestone-4.herokuapp.com/) is a sandwich fillings recipe site, giving users the ability to read recipes and filter which recipes they see, share their recipe ideas, add ingredients and allergens to the database and edit and delete recipes. There is also a data page displaying different pieces of information about the recipes, including data on what the main ingredients and allergens used in recipes are, how many recipes are vegetarian or contain meat and the different cooking times recipes need.

## UX
### User Stories
* As a user wanting to add a recipe, on the Add Recipe page there is a form which adds a new recipe to the database.
* As a user wanting to add an ingredient, when on the Add Recipe page I click on the Add ingredient button (next to the Ingredients dropdown), which takes me to the Add Ingredient page where there is a form which adds a new ingredient to the database.
* As a user wanting to add an allergen, when on the Add Recipe page I click on the Add allergen button (next to the Allergen dropdown), which takes me to the Add Allergen page where there is a form which adds a new allergen to the database.
* As a user wanting to edit a recipe, on the full recipe page of a recipe I click on the Edit button, which takes me to the Edit Recipe page where there is a form which replaces the current version of the recipe with the edited version to the database.
* As a user wanting to delete a recipe, on the full recipe page of a recipe I click on the Delete button, which deletes the recipe from the database.
* As a user wanting to view recipes, on the Recipes page I can view all the recipes in the database.
* As a user wanting to filter recipes, on the Recipes page I click on the Filter recipes button, which reveals a hidden form with categories that you can use to filter (e.g. if the recipe is vegetarian).

## Mock Ups
I created mock ups for small, medium and large screens, which are in the ['mockups' directory](https://github.com/jamesahorne/milestone_3/blob/master/mockups/milestone_3_mockup.pdf) in this project.
* I altered the website’s design slightly from the mock ups, partly because I later decided against displaying a picture of what the recipe should look like (I didn’t think this would benefit the user in making the filling). As a result of this I used an accordion to display the recipes, rather than cards.
* I also decided not to use a search field to filter recipes (I thought filtering by main ingredient, if it’s vegetarian or not and by how long it takes was sufficient).
* In the Data page I swapped a Most Popular Recipes list for a pie chart displaying which allergens contained, and used a pie chart for Main Ingredient, a bar chart for Meat vs Vegetarian and a row chart for Total Time.

## Database Schema Design
MongoDB data objects are stored as separate documents inside a collection. The collections used are:
* allergens
* ingredients
* portion_sizes
* recipes
* total_times
* vegetarian

## Features
### Existing Features
* Recipe filters – allow users to search for specific types of recipes (e.g. vegetarian recipes) by selecting one or more of the filters in the filter form.
* Reset button – allows users to reset the filter form if they don’t wish to search using a filter by clicking the Reset button.
* Add recipe – allows users to add a recipe by filling out the form on the Add Recipe page.
* Add ingredient – allows users to add an ingredient by filling out the form on the Add Ingredient page.
* Add allergen – allows users to add an allergen by filling out the form on the Add Allergen page.
* Edit recipe – allows users to edit a recipe by clicking the Edit button on the full recipe page of a recipe and then updating the form on the Edit Recipe page.
* Delete recipe – allows users to delete a recipe by clicking the Delete button on the full recipe page of a recipe.
* Data filter – allows users to filter the data on the data page by clicking on a piece of data in one of the data charts, for example clicking on the Yes bar in the Vegetarian vs Meat bar chart to see the data for vegetarian recipes.

### Features Left to Implement
In the future, I would like to implement more features.
* User registration and authentication – so only the user who posted the recipe can edit or delete it. This would also enable users to save their favourite recipes on their account.
* Include ingredient amounts – ingredients are currently stored in a separate MongoDB collection as opposed to as text, meaning that ingredient amounts aren’t as easily stored.
* Include form validation so that half-filled out forms can’t be submitted.

## Technologies Used
* HTML
    * I have used HTML to structure my website.
* CSS
    * I have used CSS to style my website, based on SCSS templates I created.
* [Materialize CSS](https://materializecss.com/)
    * I have used Materialize for the grid system and the pre-set classes, such as the navigation and button classes.
* JavaScript
    * I have used JavaScript to add interactivity to the site and for the data charts in the Data page.
* [JQuery](https://jquery.com/)
    * I have used JQuery because it is a Materialize dependency and to simplify DOM manipulation.
* [D3.js](https://d3js.org/), [Crossfilter](http://crossfilter.github.io/crossfilter/), [dc.js](https://dc-js.github.io/dc.js/) and [queue.js](https://caolan.github.io/async/queue.js.html)
    * I have used these charting libraries to create and render the interactive recipe data charts on the Data page.
* [MongoDB](https://www.mongodb.com/) and [mLab](https://mlab.com/)
    * I have used MongoDB and mLab to store and retrieve the data.
*  [Python](https://www.python.org/)
    * I have used Python as the language for the back-end code.
* [Flask](http://flask.pocoo.org/)
    * I have used Flask as the microframework to extend Python to front end with HTML templates.
* [Pencil](https://pencil.evolus.vn/)
    * I have used Pencil for creating the mock-ups.


## Testing
### Manual Testing
I decided it wasn’t necessary to automate any tests, so conducted manual tests.

1. To test that Flask has installed and is working properly, I created a test function with a route in it that will display the text "Hello World." It worked on the browser.
2. Add Recipe form:
    1. Go to the Add Recipe page
    2. Try to submit the correctly filled-out form
    3. On submission, the page is redirected to the Recipes page to find the newly added recipe at the bottom of the recipe list
3. Add Ingredient form (same process for Add Allergen form):
    1. Go to the Add Recipe page and click on the Add ingredient button, which takes you to the Add Ingredient page
    2. Try to submit the correctly filled-out form
    3. On submission, the page is redirected to the Add Recipe page.
    4. Click on the Add ingredients dropdown to find the newly added ingredient at the bottom of the ingredients dropdown
4. Edit Recipe form:
    1. Go to the full recipe page of a recipe and click on the Edit button, which takes you to the Edit Recipe page to find the current recipe detail values in the corresponding fields of the form
    2. Edit some values and submit the form
    3. On submission, the page is redirected to the Recipes page.
    4. Click on the recipe just edited to find the new recipe details have updated
5.	Delete recipe:
    1.	Go to the full recipe page of a recipe and click on the Delete button
    2. The page is redirected to the Recipes page. The recipe just deleted has disappeared from the recipes list
6.	Filter recipes form:
    1. Go to the Recipes page
    2. Click Filter recipes button to reveal hidden filter recipes section
    3. Fill out as many fields in the form as you want
    4. Either click the Filter button
        1. The recipes filter down to the recipes the meet the filter criteria
    5. Or the Reset button 
        1. The filter recipes form resets to default values

### Browser Testing
In addition to the above manual tests, I have tested this on various browsers and devices to make sure that the website is compatible on them. The website looks and functions the same on all browsers and devices except the issues below on Microsoft Edge, both of which I haven’t yet addressed, which were:
* The buttons, which should be pink, are blue.
* The Reset button in the filter recipes section, which only uses HTML (as no JavaScript is needed when type=reset), doesn’t work.

## Deployment
The website is deployed and hosted on Heroku (https://milestone-4.herokuapp.com/).
To deploy the website, follow the instructions below.
1.	Add "requirements.txt" using command "sudo pip3 freeze --local > requirements.txt" and "Procfile" using "echo web: python app.py > Procfile".
2.	Hide the environment variables (MONGO_DBNAME and MONGO_URI), by putting them in the .bashrc file. Add the same environment variable names and values into Heroku Config Vars.
3.	Initialise the repository and connect to Heroku in the terminal by terminal command “Heroku login” and subsequent adds, commits and pushes to Heroku.
4.	Start scaling dynos by command “heroku ps:scale web=1”
5.	Create environment variables IP and PORT in Heroku Config Vars
6.	Lastly I went to the website URL and tested all links and tests recorded above to confirm there are no differences between the deployed version and the development version.

## Credits
* I received inspiration for this project from several Code Institute tutors and their feedback.
* One Code Institute tutor gave me the idea for the scale variable (data.js: 56-63).
* I used code from [this website](https://www.longren.io/wrapping-text-inside-pre-tags/) to wrap text inside my pre tags.
* Inspiration from [this site](https://ficoea-cookbook.herokuapp.com/) for the Data page.
