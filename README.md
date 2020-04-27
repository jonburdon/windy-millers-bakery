# Windy Miller's Bakery - Data Centric Design

Introduction paragraph.



## [View Deployed Site](https://windy-miller.herokuapp.com/)




### [Aims & Purpose:](#aims-and-purpose)
[Developer Aims](#developer-aims), [Project Spec](#project-spec)

### [ Overview:](#overview)
[UX](#ux), [User Stories](#user-stories), [Wireframes](#wireframes)

### [ Features of the Project:](#features)
[Surface design](#surface-design), [Current Features](#current-features), [Planned Features](#planned-features)

### [ Technologies Used:](#technologies-used)
[Languages](#languages), [Libraries](#libraries), [Tools](#tools), [Hosting](#hosting)

### [ Data Structure:](#data-stucture)
[Rationale](#rationale), [Database Overview](#database-overview), [Collections](#collections), [DB Fields](#db-fields)

### [ Workflow:](#workflow)

### [ Testing:](#testing)

[Code Validation](#code-validation), [Responsiveness and Rendering](#responsiveness-and-rendering), [Browser Compatibility](#browser-compatibility), [Features Testing](#features-testing), [Unit Tests](#unit-tests)

### [ Deployment:](#deployment)
[Deployment to Heroku](#deployment-to-heroku), [Local Deployment](#local-deployment)

### [ Project Review](#review)

### [ Acknowledgements:](#acknowledgements)
[Copy](#copy), [Media](#media), [Code](#code)





## <a name="aims-and-purpose"></a> Aims & Purpose:

#### <a name="developer-aims"></a> Developer Aims

1. Apply understanding of how to use CRUD calls to mongodb using Python with Flask application
2. Build HTML based user interface to demonstrate CRUD calls in action
3. Style the above using the Materialize framework for improved UX
4. Build the project in a time efficient and effective manner to meet initial spec precisely, enhancing this with 'nice to have' features only if time allows.

#### <a name="project-spec"></a> Project Aims

###### Credit: Adapted from Code Institute project spec)
1. Data handling: Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain.
2. Database structure: A database structure well-suited for the data domain of a recipe book website.
3. User functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality).
4. Use of technologies: Use HTML and custom CSS for the website's front-end.
5. Structure: Incorporate a main navigation menu and structured layout. This may be achieved with Materialize / Bootstrap
6. Version control: Use Git & GitHub for version control.
7. Deployment: Deploy the final version of code to a hosting platform - Heroku.


 ## <a name="overview"></a> Overview

 #### <a name="ux"></a>UX

### Scope agreed with (fictitious) client prior to project start:
### Site Owners Goals
1. Promote a brand of kitchen utensils

### Minimum deliverable:
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


#### Fictitious client brief agreed before build - Site Minimum Functions
1. Implements grid view of recipes. Visual design to be agreed with client / designer / developer before development work starts.
2. Displays three recipe categories by title with recipes and 'ALL' recipe display. Each category to be viewed separately, or view all option (default).
3. Sort by recipe name, or cooking time

### Fiction client brief agreed before build - Potential advanced features (nice to have):

1. [x] Build upon the required tools field to promote your brand of kitchen tools (e.g. oven, pressure cooker, etc…). Display detail on the utensil itself on a single page view for this utensil
2. [x] Create a dashboard to provide some statistics about all the recipes. Number of recipes, number in each category, utensils, number of recipes using this utensil
3. [ ] Pagination for more than 20 recipes.
4. [ ]  Sort by name or cooking time in ascending / descending order.
5. [ ] Add 'similar recipes' display on single recipe view
6. [x] Display 'Featured utensils' on home page
7. [ ] Carousel display on home page with interactive swipe navigation
8. [ ] Add facility to log in order use a provided pin before editing / deletion is permitted. 
9. [x] Header is 'sticky' and shrinks on scroll
10. [x] Background or hero header image parallax effect
11. [ ] CTA tab bar floating / sticky on right of screen to encourage user to navigate to utensils page.
12. [ ] Update form to verify all form fields and only accept forms accordingly.
13. [x] Confirmation messages when data has been added / updated / deleted. Delete confirm message.
14. [x] Featured Recipe option
15. [ ] Facility to convert units from metric to imperial
16. [x] Add animation to the sorting, filtering and displaying of data 
17. [x] Delete function will only mark recipe as 'archived.' To permanently delete, user must enter archive manager and then permanently delete the item.
18. [ ] Submit image through form and use Cloudinary to host images. API Documentation here: https://cloudinary.com/documentation/cloudinary_references

 #### <a name="user-stories"></a> User Stories

##### As a customer looking for recipes I want to be able to

1. Easily learn how to navigate the different recipes
2. Find the type of recipe I am interested in quickly
3. Add my own recipes to the database
4. Get reassuring feedback when I update the database (edit, add, delete)


#### <a name="wireframes"></a> Wireframes

A wireframe for the project can be viewed here: ![](static/wireframes/wireframe.jpg)
This wireframe is very early inspiration and represents only a first stage of design and planning.


 ## <a name="features"></a> Features of the Project:

 ### <a name="current-features"></a> Current Features

#### <a name="surface-design"></a> Surface design

The surface design of the project varied from the wireframes to some degree - a sidebar was used on the recipe page but not for searching or filtering. 

The recipes section of the [Doves Farm](https://www.dovesfarm.co.uk/recipes?view=all) website was used for reference and some design inspiration. A soft, calm colour palette was selected with eggshell blue and brown tones. A brighter highlight colour was selected for the primary CTA area - to browse utensils from the home page.

Simplicity of design holds user attention more according to research read by the developer, so plenty of negative space was added throughout - consistent sizing  of fonts and padding creates a hierarchy of content types.

Icons were used to give visual reference right from the front page - the same icons are used throughout for Recipes, Utensils and Categories.

A Hero header with parallax effect was added to the top of each page to give reassurance to the user and make the site appearance easily predictable.


##### Front End Features
##### Home Page
##### UX
1. Nav Bar is sticky (top). This ideas on vertical scroll, and reappears when the user scrolls up from any scroll position.
2. Mobile modal popup alternative menu.
3. Hero header area with background image, box shadow text and parallax effect.
4. Icon graphics are used to establish a visual convention on the home page for Recipes, Categories, Utilities and 'Add.' This convention is maintained throughout the site.
5. Filtering and sorting of recipe items is displayed on the home page, using isoptope js library. The 'Add your own' CTA box will always appear last.
6. Data dashboard section displays recipe data.
7. Floating action buttons for database management tools.
8. 'Feature Discovery' draws attention to the floating action buttons when 'add' button is clicked within a page or on the 'Add' menu item.
9. Components - A Quote box, data dashboard and CTA box are added as resueable components and are then visible on different pages throughout the site. This gives the site owner control and facilitates potential for quick and easy addition of targetted marketting content.
10. About page - left / right two column view switches the order of the content responsively to a stacked one column alternating view of images and body copy on mobile view.
11. Lottie files animation uses json data only to add an animation resulting in faster load times.
12. Footer - standard on all pages, includes external links to socal pages and a simple one item footer link (internal).
13. Recipe pages template - containing sidebar with featured recipes
14. Category single page template - containing section with other recipes from this category
15. Categories page - containing grid view with links to single category pages
16. Utensil pages template - containing badge for 'delux' utensils, external link to shop url, section with other recipes with this featured utensil, section linking to all utensils
17. Utensils page - containing grid of all utensils with links to single utensil pages view or external links to 'buy' utensils

##### Front end database management features
1. Recipes, Categories and Featured Utensils can be added, deleted and updated in the database.
2. Recipes, Categories and Featured Utensils can be 'archived.' In this case they are marked as *'unpublished'* in the database. Before final deletion, a *final confirmation* message is displayed to warn the user and confirm twice.

##### CSS Custom Properties
1. CSS custom properties used to provide a colour palette. Color codes are written once, at the top of the css file, and then referred to using var() throughout the rest of the code.


#### Back End Features


1. [x] Build upon the required tools field to promote your brand of kitchen tools (e.g. oven, pressure cooker, etc…). Display detail on the utensil itself on a single page view for this utensil
2. [x] Create a dashboard to provide some statistics about all the recipes. Number of recipes, number in each category, utensils, number of recipes using this utensil
3. [x] Display 'Featured utensils' on home page
4. [x] Header is 'sticky' and shrinks on scroll
5. [x] Background or hero header image parallax effect
6. [x] Confirmation messages when data has been added / updated / deleted. Delete confirm message.
7. [x] Featured Recipe option
8. [x] Add animation to the sorting, filtering and displaying of data 
9. [x] Delete function will only mark recipe as 'archived' by changing 'published' field in the db from on to off. To permanently delete, user must enter archive manager and then permanently delete the item.

 ### <a name="planned-features"></a> Planned Features


1. Pagination for more than 20 recipes.
2. Sort by name or cooking time in ascending / descending order.
3. Add 'similar recipes' display on single recipe view
4. Carousel display on home page with interactive swipe navigation
5. Add facility to log in order use a provided pin before editing / deletion is permitted. 
6. CTA tab bar floating / sticky on right of screen to encourage user to navigate to utensils page.
7. Update form to verify all form fields and only accept forms accordingly.
8. Facility to convert units from metric to imperial
9. Submit image through form and use Cloudinary to host images. API Documentation here: https://cloudinary.com/documentation/cloudinary_references
10. Add a hierarchy to the recipe database categories collection so that 'Sourdough' and 'Yeast Breads' could be organised under the main category of 'Bread.'
11. Add array items to the recipe ingredients so that individual ingredients and their quanitities can be added or deleted as individual fields in the database. Use the same functionality for steps in the recipe method.



 ## <a name="technologies-used"></a> Technologies Used:

 #### <a name="languages"></a> Languages

* [HTML 5.0](https://www.w3.org/Style/CSS/)
* [CSS](https://www.w3.org/Style/CSS/) - style the html and add interactivity
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - used for manipulating the DOM
* [Python 3](https://www.python.org/) - Used for back end application
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - the templating language

 #### <a name="libraries"></a> Libraries & Frameworks
* [Flask 1.0.2](https://flask.palletsprojects.com/en/1.1.x/) - A micro web server framework
* [Pymongo 2.3.0](https://flask-pymongo.readthedocs.io/en/latest/) - Used to perform C.R.U.D. operations in Mongo DB using python
* [Materialize 0.100.2](http://archives.materializecss.com/0.100.2/) - CSS framework for front end
* [jQuery](https://jquery.com/) - used for enhanced interactive features
* [Flex](http://flexboxgrid.com/) - used to achieve responsive layout on About page
* [Isotope](https://isotope.metafizzy.co/) - used to add sorting and filtering of grid items on the home page
* [Animate on Scroll Library](https://michalsnik.github.io/aos/) - add animations on scroll
* [Lottie Files](https://lottiefiles.com/) - Used as source for json based animation files and embedded player

 #### <a name="tools"></a> Tools
* [Git](https://git-scm.com/) - for version control
* [Github](https://github.com/) - provide hosting for development using Git
* [Mongodb](https://www.mongodb.com/cloud/atlas) - the database server used
* [VSCode](https://code.visualstudio.com/) - Local IDE
* [uPic](https://apps.apple.com/us/app/upic-image-compression/id1341586328?mt=12) - used for Image compression
* To pick colours from image when building colour scheme: https://imagecolorpicker.com/


 #### <a name="hosting"></a> Hosting

* [Heroku](https://www.heroku.com/) - for hosting

 ## <a name="data-stucture"></a> Data Structure:

 #### <a name="rationale"></a> Rationale

One main for the project for the developer was to keep the projects simple and work to find the minimum level fo complexity needed to deliver a result. For this reason, each data field in the recipe collection is a single string field. This meant the form to dict methof could be used to send data straight from the form to the database rather that manipulating the form data programatically before submitting it.

 #### <a name="database-overview"></a> Database Overview

The data is organised on Mongo db in three collections: Recipes, Categories and Utensils.

Consideration was given to adding individual ingredients and separate steps in the recipe method as array items within a custom field in the recipe collection. Ingredient quantities were also considered. This feature could be added in a future release.

Consideration was given to other collections such as 'Regions of the World,' or 'Difficulty.' Two types of Bread exist as separate categories - Sourdough and Bread. And improved data structure might use a hierarchy of categories so that Soughdough and Yeast Breads exists as sub categories within the main 'Bread' category. This feature could be added in a future release.

 #### <a name="collections"></a> Collections

The Recipes collectioncontains string variables relevant to a single recipe. The category field is used to match the document with that name in the categories collection. There is a data field for utensils and a separate field for featured utensils. This field is matched to the document of the same name in the utensils collection. 

The Utensils collection contains documents for individual 'featured utensils' which can be selected as fields and referenced by name in the 'featured- utensil' field in recipes collection. 

 #### <a name="db-fields"></a> DB Fields 

##### Recipes Collection

* recipe_name
* recipe _description
* recipe_serves
* category_name
* utensil_list
* featured_utensil
* ingredients_list
* method
* preparation_time
* cooking_time
* tips
* photo_url
* published
* featured

##### Categories Collection

* category_name
* catrgory_image
* published

##### Utensils Collection

* utensil_name
* utensil_description
* image_url
* delux_range
* shop_url
* published



## <a name="workflow"></a> Workflow: 

A process of progressive enhancement was followed, using the following working process.

### Working Process:
1. CRUD Operations Stage

Sample data was added to the database. Create, Read, Update and Delete functions were written. These functions were manually tested.

No attention was paid to front end design. Only minimal grids and boxes were visible.

2. Integrating Frameworks - Materialize, Isotope

The isotope js framework was the main framework selected for improved UX. The functionality for this was added and tested first. Once this was installed, materialize components and grid were added.

3. Customised Front End

The Materialize grid was added to the Home Page first, followed by other features - navbar, floating action buttons etc. Custom css was used for the hero area. CSS was developed for different content sections with appropriate colours and margins / padding. Each feature added was tested on different devices. Once features were fully working on the home page, other pages were built.

4. Content Migration


5. Final enhancements

Time was taken to add optional, more advanced features beyond the basic requirements:
* Images for featured utensils at top of home page change when buttons are hovered
* Data dashboard
* Useseable components
* Animate on Scroll
* Buttons grow on hover



 ## <a name="testing"></a> Testing: 


### Testing protocol for each page

The following manual testing protocols were followed for each page on desktop, mobile, tablet and smart TV devices.

* *All links navigate to correct destination*
* desktop and mobile menus.
* All utensils page
* All categories page
* About page
* Manage page
* Archive page
* Add recipe, add category, add utensil
* Single recipe pages
* Single category pages
* Single utensil pages

* *Page content*
1. Resize the width of the browser and verify that the content resizes for different screen sizes as expected.
2. Verify that any content that should be hidden on smaller screens is hidden.
4. Verify there is no overflow.

* *Navigation Buttons*
1. Verify that each button correctly displays the content when clicked.
2. Verify that each button displays a box shadow and changes position when clicked.
3. Change the width of the browser to ensure the navbar collapses when expected.
4. Hover over buttons and verify that cursor: pointer is active.
5. Verify that text is readable on different screen sizes.

A dead link checker was used to check for dead links. http://www.brokenlinkcheck.com/

During testing, an old link was found on the mobile popup menu.
During testing, the edit form page was found to be using an out of date styling.

 #### <a name="code-validation"></a> Code Validation 

* To validate html: https://validator.w3.org/
* To validate css: https://jigsaw.w3.org/css-validator/
* To check Javascript for errors: https://www.jslint.com/

Note: The css validator throws errors relating to use of :root, var and also some webkit prefixes. These do not affect the project's performance.



 #### <a name="responsiveness-and-rendering"></a> Responsiveness and Rendering

 #### <a name="browser-compatibility"></a> Browser Compatibility

* http://www.cssdrive.com/cssautoprefixer/


 #### <a name="features-testing"></a> Features Testing

 The following features were tested:
* When a recipe is added using the Add Recipe form, this recipe is displayed in the front end.
* When a utensil is added using the Add Utensil form, this utensil is displayed in the front and is available as a select field when adding new recipes.
* When a category is added using the Add Category form, this category is displayed in the front end, is available as a select field when adding new recipes and is available as a filter option on the front page.
* Archiving: When a recipe, category or utensil is selected for archiving, the item is hidden on the home page but is visible in the Archive Manager page.
* Restoring from archive: When a recipe, category or utensil is selected for restore, the item is hidden from the archive but is again visible on the home page.
* Deleting: When a recipe, category or utensil is deleted permanently, this is removed from mongodb.


 #### <a name="unit-tests"></a> Unit Tests 

Unit testing was not carried out. The developer familiarised himself with the following technical documentation and tutorials but did not implement this process:
* https://pythonhosted.org/Flask-Testing/
* https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three#toc-tests


 ## <a name="deployment"></a> Deployment: 


#### <a name="deployment-to-heroku"></a> Deployment to Heroku
##### Database Setup

Create database on mongodb cloud

Get data in place first, on atlas mongo website:
* database with two collection: categories and tasks
* Create a sample record in category collection called category_name: "Home"
* Create sample record in the task collection with category_name, task_name, task_description, is_urgent and due_date


##### Setup using VS Code on a Mac
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

##### Deploying to Heroku
###### Four steps to deploying in Heroku
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

##### Connecting to MongoDB Atlas

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


Create an instance of pymongo, add app with constructor method.

    mongo = Pymongo(app)



 #### <a name="local-deployment"></a> Local Deployment 

With the above setup, to deploy locally on a mac:

1. Open a terminal for the virtual environment where the project resides
2. Type python3 app.py 
3. Browse to http://0.0.0.0:5000/ 



 ## <a name="review"></a> Project Review, April 27th 2020:

A brief review follows, based on the developer's own aims.
1. Apply understanding of how to use CRUD calls to mongodb using Python with Flask application
This made a good opportunity to revise basic CRUD calls from python. Comments were added during the process to ensure that the code is easy to understand, maintain, and use for future reference. The form_to_dict method was used to take form data and add this to the database. The method does not handle data from multi select check boxes, which meant a small change to design was needed - only one 'Featured Utensil' could be chosen. In the future, it would be beneficial to use a different method to add form data to mongo.

2. Build HTML based user interface to demonstrate CRUD calls in action
Jinja tags were added to the html-attributes to facilitate use of the isotope js library for filtering and sorting. Adding the About page was an opportunity to use a slightly different visual layout and use flex CSS. The left and right alternating columns used on desktop view cause a visual problem when stacked on mobile (two images columns appear consecutively when stacked) unless flex-display: col-reverse is used. The meant adding cross vendor prefixes.

3. Style the above using the Materialize framework for improved UX
1.0.2 was used. This meant jquery version required did not cause problems with that required for isotope js. The following components of the Materialise framework were utilised:
* Grid
* Helpers - vertical-align, hover, responsive-img
* CSS Components - Cards, Collections, Footer, Forms, Navbar
* JS - Feature discovery, modal
The developer found the framework well documented, powerful, and easy to install. Using 0.100.2 meant it was easy to install alongside other js libraries - isotope and animated on scroll.

4. Build the project in a time efficient and effective manner to meet initial spec precisely, enhancing this with 'nice to have' features only if time allows.
An essential aim for the developer was to deliver the project to a high standard in a minimal amount of time. This aspects of the project went well. It was started on the 11th of March and completed by the end of April. 1-2 days per week only were allocated. Planning the workflow in the stages outlined above helped. It was easy to get distracted by advanced features that were not necessary for the minimum requirements. Some advanced features such as search and pagination were not included due to time restraints. The most time consuming elemenets were:
* Data dashboard - displaying only those recipes with less than 15 minutes cooking time.
* Selecting only recipes with the same utensil, or only recipes from this category - to display on specific pages.
* Adding isotope js filtering and sorting.




 ## <a name="acknowledgements"></a> Acknowledgements:

 #### <a name="copy"></a> Copy 

 #### <a name="media"></a> Media

### Credits
https://en.wikibooks.org/wiki/Cookbook:Table_of_Contents
https://pixabay.com/

#### Colour Palette:
The following image was used for colour palette inspiration:
https://www.pinterest.co.uk/pin/524880531556508076/
The website https://imagecolorpicker.com/en/ was used to autogenerate a wider range of colour codes from the original reference image.

#### <a name="code"></a> Code 

* Materialize snippets were used extensively from the site documentation and then altered using progressive enhancement.
* Other small snippets are attributed in the code comments


### Technical Reference 
https://caniuse.com/
https://css-tricks.com/
https://docs.mongodb.com/manual/reference/
https://www.w3schools.com/
Add more here eg flex
Stack Overflow
Convert hex to rgb, rgba:
https://www.hexcolortool.com/



## Known issues:

Sort by cooking time not working.

