# Windy Miller's Bakery - Data Centric Design


[View Site on Heroku](https://windy-miller.herokuapp.com/)

## Project Aims / Minimum Requirements:

1. Data handling: Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain.
2. Database structure: A database structure well-suited for the data domain of a recipe book website. Use appropriate nesting relationships between records of different entities.
3. User functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality).
4. Use of technologies: Use HTML and custom CSS for the website's front-end.
5. Structure: Incorporate a main navigation menu and structured layout. This may be achieved with Materialize / Bootstrap
6. Documentation: Provides detail on what the project does and the value that it provides to its users.
7. Version control: Use Git & GitHub for version control.
8. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
9. Deployment: Deploy the final version of your code to a hosting platform - Heroku.

## Developer Aims
1. Apply understanding of how to use CRUD calls to mongodb using Python with Flask application
2. Build HTML based user interface to demonstrate CRUD calls in action
3. Style the above using the Materialize framework for improved UX
4. Document the project for future reference
5. Build the project in a time efficient and effective manner to meet initial spec precisely, enhancing this with 'nice to have' features only if time allows.

## Technologies used
* HTML, CSS and Javascript programming languages
* Python
* Mongodb
* Flask
* Materialize
* [Bootstrap](https://getbootstrap.com/)
* [Font Awesome](https://fontawesome.com/)
* [Flex](http://flexboxgrid.com/) as implemented through Bootstrap 4
* [VSCode](https://code.visualstudio.com/) Files were created locally using Visual Studio. GIT was used to push files to Github
* [jQuery](https://jquery.com/) was used throughout, particularly to watch for events in the DOM and react accordingly.
* [Popper.js](https://popper.js.org/) was loaded by Bootstrap in order to implement the collapsable navbar
* [Git](https://git-scm.com/)

### Tools used for automation
- To validate html: https://validator.w3.org/
- To validate css: https://jigsaw.w3.org/css-validator/
- To check Javascript for errors: https://www.jslint.com/
- To pick colours from image when building colour scheme: https://imagecolorpicker.com/



## Scope agreed with (fictitious) client prior to project start:
### Credit: Adapted from Code Institute project spec)

## User Stories
### As a customer looking for recipes I want to be able to

1. Easily learn how to navigate the different recipes
2. Find the type of recipe I am interested in quickly
3. Add my own recipes to the database
4. Get reassuring feedback when I update the database (edit, add, delete)

### Site Owners Goals
1. Promote a brand of kitchen utensils

### Minimum:
1. Create a web application that allows users to store and easily access cooking recipes. Recipes would include fields such as ingredients, preparation steps, required tools, cuisine, etc.
2. Create the backend code and frontend form(s) to allow users to add new recipes to the site, edit them and delete them.
3. Create the backend and frontend functionality for users to locate recipes based on the recipe's fields. You may choose to create a full search functionality, or just a directory of recipes.
4. Provide results in a manner that is visually appealing and user friendly.

### Site Structure

#### Pages
* Home
* Search
* Recipes
* Utensils
* Carousel (advanced optional feature)
* Responsive grid displays in fewer columns on tablet / mobile

#### Header
* Appears identical on all pages
* Hamburger style on mobile
* Include CTA button to promote utensil products

#### Footer
* First Column:
* Social Media links
* Privacy Policy
* Terms and Conditions
* Login (advanced features)
* Second column with Category options
* Third column with Utensil Products view


#### Site Minimum Functions
1. Implements accordion or tab style display. Visual design to be agreed with client / designer / developer before development work starts.
2. Displays three recipe categories by title with recipes and 'ALL' recipe display.
3. Sort by recipe name, or cooking time

### Potential advanced features (nice to have):
1. Build upon the required tools field to promote your brand of kitchen tools (e.g. oven, pressure cooker, etc…). Display detail on the utensil itself on a single page view for this utensil
2. Create a dashboard to provide some statistics about all the recipes.
3. Pagination for more than 20 recipes.
4. Sort by name or cooking time in ascending / descending order.
5. Add 'similar recipes' display on single recipe view
6. Display 'Featured utensils' on home page
7. Carousel display on home page with interactive swipe navigation
8. Add facility to log in order use a provided pin before editing / deletion is permitted. 
9. Header is 'sticky' and shrinks on scroll
10. Background or hero header image parallax effect



## Developer ideas for enhancing project / next steps and advanced features:
1. [] Update form to verify all form fields and only accept forms accordingly.
2. [] Confirmation messages when data has been added / updated / deleted. Delete confirm message.
3. [] Featured Recipe option
4. [] Facility to convert units from metric to imperial
5. [] Add isotope.js to animate the sorting, filtering and displaying of data





## Wireframes

## Deployment: Process followed to set up database connection and deploy project to heroku

### Database Setup

Create database on mongodb cloud

Get data in place first, on atlas mongo website:
* database with two collection: categories and tasks
* Create a sample record in category collection called category_name: "Home"
* Create sample record in the task collection with category_name, task_name, task_description, is_urgent and due_date


### Setup using VS Code on a Mac
* **sudo pip3 install Flask** to install Flask
* **python3 -m venv env** to install virtual environment in that folder
* Open command palette, type **Python: Select Interpreter** and select the virtual environment in your project folder that starts with ./env or .\env
* In command pallette, run **Terminal: Create New Integrated Terminal**
* Install Flask in the virtual environment with **pip3 install Flask**
* **pip3 install flask_pymongo**
* Create app.py (In flask, the convention is to use run.py or app.py)
* **from flask import Flask** to import Flask in app.py Capital F indicates a class name.
* Create instance of flask within app.py with **app = Flask(name)**
* In Terminal **python3 -m flask run** to run the app and serve

### Deploying to Heroku
#### Four steps to deploying in Heroku
1. Create Heroku app
2. Link git repo
3. Create requirements.txt
4. Create Procfile


In terminal:

    heroku login

Use browser to log in

    heroku apps

In terminal

    git init
    git add .
    git commit -m 'Initial commit'
    heroku git:remote -a windy-miller
    git push heroku master (fails - needs requirements.txt)
    sudo pip3 freeze --local > requirement.txt
    git add .
    git commit -m 'Added requirements'
    git push heroku master (fails - needs procfile)
    echo web: python app.py > Procfile
    git push heroku master
    heroku ps:scale web=1

On Heroku web interface:
Specify IP 0.0.0.0 and Port 5000

### Connecting to MongoDB Atlas

    sudo pip3 install flask-pymongo
    sudo pip3 install dnspython
    
    
in new file env.py:
	import os
	os.environ["MONGO_URI"] = "mongodb+srv://databaseusernameHERE:passwordforthatuserHERE@myfirstcluster-ghyoe.mongodb.net/databasenameHERE?retryWrites=true&w=majority"

*NOTE* Formatting of connection string carefully. No <> around password, there are THREE places to insert the correct into in to the connection string.


in app.py this will read the needed variables from the env.py file, created above):

	from os import path 
	if path.exists("env.py"):
    import env

    from flask_pymongo import PyMongo
    from bson.objectid import ObjectId

	app.config["MONGO_DBNAME"] = 'windy-millers_bakery'
	app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

On Mongo Website: Overview -> Connect -> Connect my app -> Choose Python3.6 or later

Copy connection string

Paste in connection string

**Ensure an environment variable for above is used when in production**
**Database mini project was set up using an environment variable**

Create an instance of pymongo, add app with constructor method.

    mongo = Pymongo(app)