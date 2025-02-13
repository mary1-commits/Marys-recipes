Mary's Recipes - Share Your Culinary Creations!
A fully responsive Django web application that allows users to share, review, and comment on their favorite (or least favorite) recipes. Users can create their own recipe posts, interact with other users through comments, and explore a collection of dishes from around the world.

Screenshot of Site
(Insert screenshot here)

Deployed Link
https://authentic-recipe-457331f032d1.herokuapp.com/

Contents
UX - User Experience
User Stories
Wireframes
Design
Accessibility
Fonts
Database Planning
Key Features
General
Recipes
Comments
Future Features
AI Implementation
Testing
Deployment
Heroku
PostgreSQL
Technologies Used
Credits
Acknowledgements
UX - User Experience
User Stories
User Story	Description	Priority
Account Registration	As a site user, I want to register for an account so that I can post and save my recipes.	Must Have
Recipe List	As a site user, I want to view a list of all available recipes so that I can explore new dishes.	Must Have
Detailed Recipe Page	As a site user, I want to click on a recipe to view full details, including ingredients and instructions.	Must Have
Create Recipes	As a site user, I want to be able to submit my own recipes so that I can share them with others.	Must Have
Edit & Delete Recipes	As a site user, I want to be able to edit and delete my recipes so that I can update or remove them.	Must Have
Post Comments	As a site user, I want to comment on recipes so that I can interact with the community.	Must Have
Moderate Comments	As a site admin, I want to approve or delete comments so that I can maintain a positive environment.	Must Have
Pagination	As a user, I want the recipe list to be paginated so that I can browse easily.	Should Have
Recipe Categories	As a user, I want recipes to be categorized (e.g., desserts, main courses) so that I can find specific types of dishes.	Should Have
Like & Favorite Recipes	As a user, I want to save my favorite recipes so that I can easily find them later.	Could Have
Wireframes
Mobile Wireframes: (Insert images here)
Tablet Wireframes: (Insert images here)
Desktop Wireframes: (Insert images here)
Design
Color Scheme
#1a3c40 – Deep Green
#f4eae0 – Soft Beige
#c08457 – Warm Brown
#e1b382 – Light Brown
#a15c38 – Rustic Orange
Coolors was used to help finalize the color palette.

Accessibility
Semantic HTML: Proper heading structures and meaningful elements.
Color Contrast: Checked for readability.
Responsive Design: Works across all screen sizes.
Fonts
Playfair Display: For headers, giving an elegant and refined touch.
Lato: A clean and readable sans-serif for body text.
Database Planning
Models
User – Stores user information.
Recipe – Contains details about each recipe (title, description, ingredients, instructions, image, etc.).
Comment – Stores user comments on recipes.
Key Features
General
Navbar: Navigation links to Home, Recipes, Create Recipe, Login/Logout.
Footer: Displays copyright and project name.
Recipes
CRUD Functionality: Users can create, read, edit, and delete their own recipes.
Image Uploads: Recipes include an image upload feature.
Search & Filters: Users can search for recipes or filter by categories.
Recipe Details Page: Displays recipe title, ingredients, instructions, and comments.
Comments
CRUD Functionality: Users can post, edit, and delete comments.
Moderation: Admins can approve or delete inappropriate comments.
Future Features
User Profiles: Users will have profiles showing their submitted recipes and interactions.
Recipe Ratings: A 5-star rating system for recipes.
Shopping List Generator: Users can generate a shopping list from recipe ingredients.
AI-Powered Recommendations: Suggest similar recipes based on user preferences.
AI Implementation
AI tools like GitHub Copilot were used for:

Assisting in writing Django models and views.
Troubleshooting form validation issues.
Helping structure JavaScript functions for interactivity.
Challenges faced with Copilot:

Occasionally generated incorrect function names.
Required manual debugging for Django template errors.
Testing
See TESTING.md for details on manual testing, validators, and Lighthouse results.

Deployment
Heroku
Steps for deploying on Heroku:

Install dependencies:
bash
Copy
Edit
pip install gunicorn django-heroku
Create requirements.txt:
bash
Copy
Edit
pip freeze > requirements.txt
Create a Procfile:
bash
Copy
Edit
web: gunicorn marys_recipes.wsgi
Set up Heroku:
bash
Copy
Edit
heroku create marys-recipes
Configure environment variables in Heroku:
ini
Copy
Edit
DISABLE_COLLECTSTATIC=1
DATABASE_URL=your-database-url
SECRET_KEY=your-secret-key
DEBUG=False
Deploy from GitHub or push manually:
bash
Copy
Edit
git push heroku main
PostgreSQL
The project uses a PostgreSQL database for storing user and recipe data.

Technologies Used
Django: Web framework for the application.
PostgreSQL: Database management system.
Heroku: Deployment platform.
Bootstrap: Front-end framework for styling.
GitHub: Version control and repository hosting.
Pillow: Image processing library for handling recipe images.
Summernote: WYSIWYG editor for recipe descriptions.
Credits
Images
Recipe images from Unsplash & Pexels.
Code References
Used Django documentation for authentication and form handling.
Referenced "I Think, Therefore I Blog" tutorial for comment functionality.
Acknowledgements
A big thank you to:

My fellow developers for their feedback and ideas.
Django community for detailed documentation.
Friends & family for testing and suggesting features.
