# Ecopost

## CONTENTS

* [Overview](#overview)
* [User Stories](#user-stories)
* [Features in Nutshell](#features-in-nutshell)
* [Wireframes](#wireframes)
* [Notes on the Design](#notes-on-the-design)
* [Each Part and Function in Detail](#each-part-and-function-in-detail)
* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)
- - -

![ecopost-home](media/ecopost-home.png)

## Overview
This application offers a platform where individuals around the world can share their stories on what they are doing to protect the environment. Many people feel helpless, thinking that individuals cannot do so much. Here, visitors can read posts written by others, leave comments and write their own stories. Users can connect with others who are concerned about the environmental crisis, get motivated to take actions, or at least find some hope.

## User Stories

User stories can be found [here.](https://github.com/users/rkyzk/projects/8)

## Features in Nutshell:
Users can see lists of excerpts from
- featured stories
- posts published in the previous 7 days
- popular stories of all time
- posts written by them
- posts commented by them
- posts bookmarked by them

Users can read the entire content of published posts<br>
Users can search stories by title, authors and other factors<br>
Users can sign up to become members<br>
Members can like and bookmark posts<br>
Members can leave comments on the posts<br>
Members can write their own stories and submit them<br>
Members can edit and delete comments<br>
Members can update or delete their posts before submitting them<br>

## Wireframes
Wireframes for the app can be found [here.](https://wireframe.cc/pro/pp/873798723651976)
Please click on "Homepage" in the upper left corner to see wireframes of different pages of the app.

## Notes on the Design 
The overall appearance is kept simple and clean so as not to interfere with various colors that the featured images will bring in.

**About the Colors**
- I used beige (rgb(141, 111, 56)) for the navigation menu, headings and buttons.
- I used blue (color: rgb(46, 122, 145)) for links in the text.
- I used light grey (#e8e8e8) for the footer.
- Beige and blue were chosen because they are associated with nature.

**About the Fonts**
- Montserrat Alternates was used for headings because it's stylish and visually pleasant when used sparingly.
- For the content Lato is used since it's readable and familiar. 

## Installed libraries and dependencies

gunicorn
gunicorn is the server used to run this Django project on Heroku.
dj_database_url and psycopg2 are libraries needed for PostgreSQL
cloudinary  library
django_countries for dropdown menu of countries
django-summernote
django-crispy-forms

## Manual Testing

update comment cancel --> will not be updated