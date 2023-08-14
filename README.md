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
I conducted manual testing for the aspects that weren't covered by automated testing.

### Testing User Stories
**As Users**
No. | Goals | How they are achieved | 
|:---| :--- | :--- |  
|1| What the site is for and how to use it are clear. | An introductory paragraph on the home page describes what the site is for and how to use it.  Also the links in the navigation bar indicate which page has which functionality so users can easily understand how to use the app. | 
|2| Visitors can sign up. | An introductory paragraph on the home page invites users to become a member.  In addition, a link to sign up page is displayed in the navbar. | 
|3| Featured posts are presented on the home page. | Three featured stories chosen by editors are displayed on the home page. |
|4| Users can see the list of recently published posts. |By clicking the link on the home page 'More Stories from this week' users can see the list of recently published posts. | 
|5| Users can see the list of popular posts. | By clicking the link on the home page 'Readers' favorite storeis of all time' users can see the list of the posts that have been liked the most. |
|6| Users can write posts. | On ‘Write Stories’ page logged-in users can write their own posts and submit them.  The posts will be published if admin of the site approves of them. |
|7| Users can edit posts. | By clicking 'update' on the post_detail page, users can edit their posts. |
|8| Users can delete posts. | By clicking 'delete' on the post_detail page, users can delete their posts.|
|9| Users can write comments. | Logged-in can leave comments on the post_detail page.|
|10| Users can edit comments | By clicking the edit icon, users can delete their comments. |
|11| Users can delete comments. | By clicking the trash bin icon, users can delete their comments. |
|12| Users can search posts. | On "Search Stories" page, users can search posts by multiple factors. |
|13| Users can like posts. |By clicking the heart icon, 
logged-in users can like posts.|
|14| Users can bookmark posts. |By clicking the bookmark icon, logged-in users can bookmark posts.  The bookmarked posts will be displayed on 'My Page'.|
|15| Users have easy access to 1) posts witten by the user 2) posts commented by the user and 3) posts bookmarked by the user |'My page' lists the three groups of posts.|

**As admin**
No. | Goals | How they are achieved | 
|:---| :--- | :--- |  
|16| Admin can select posts to be published. | Posts’ status is set to ‘Submitted’ when users submit their drafts, and they will not be displayed in public.  Only when admin changes the status to ‘Published,’ the posts will be publicized. |
|17| The most interesting posts are presented on "Home" |Three featured stories chosen by admin will be displayed on the home page. |
|18| Allow users to update or delete posts only before submission | Update and Delete buttons for posts appear only if posts are in ‘draft’ status.|
|19| Allow only the authors to update/delete the posts & comments | LoginRequiredMixin and UserPassestestMixin allow only the users who are logged in as the authors of the posts and comments to update or delete their writings. |
|20|Allow users to access only their own “My page” | LoginRequiredMixin and UserPassestestMixin will allow users to access only their own “My Page.” |

### Testing Features
As preparatory steps for the following tests:
1. create a user with username "testuser" and a password "gR48NmYr1". (Leave the email blank.)
2. Log in as "testuser"
3. make 10 posts with the following field values:
title: blog 1, blog 2, blog 3, blog 4, blog 5, blog 6, blog 7, blog 8, blog 9, blog 10
content: (for all of them): test content
city: Dublin
country: Ireland
4. go to admin panel.
5. publish blog 1-10 one by one in the order.
6. set featured_flag True for blog 1-3.
7. go to "Detail Page" of blog 4-10 and click on 'like' button
8. Log out

#### Navigation links

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Logo link|Go to “Search Stories”|Click on the logo|Redirected to the home page|Redirected to the home page|pass|[image](./media/manual-tests/Navlinks/1.png)|2023/8/14|
|2|”Home”|Go to “Search Stories” page|Click on “Home”|Redirected to ”Home"|Redirected to ”Home”|pass|[image](./media/manual-tests/Navlinks/2.png|2023/8/14|
|3|”Search stories”|Go to “Home”|Click on “Search Stories”|Redirected to ”Search Stories”|Redirected to ”Search Stories”|pass|[image](./media/manual-tests/Navlinks/3.png)|2023/8/14|
|4|”Become a Member”|Go to “Home” page|Click on “Become a Member”|Redirected to ”Become a Member” | Redirected to “Become a Member”|pass|[image](./media/manual-tests/Navlinks/4.png)|2023/8/14|
|5|”Sign in”|Go to “Home” page|Click on “Log in”|Redirected to ”Log in”|Redirected to “Sign in in”|pass|[image](./media/manual-tests/Navlinks/5.png|2023/8/14|
|6|”Write Stories”|Log in and go to “Home” page|Click on “Write Stories”|Redirected to ” Write Stories”|Redirected to ” Write Stories”|pass|[image](./media/manual-tests/Navlinks/6.png)|2023/8/14|
|7|”My Page”|Go to “Home” page|Click on “My Page”|Redirected to ”My Page”|Redirected to “My Page”|pass|[image](./media/manual-tests/Navlinks/7.png|2023/8/14|
|8|”Sign out”|Go to “Home” page|Click on “Sign out”|Redirected to ”Log out”|Redirected to “Sign out”|pass|[image](./media/manual-tests/Navlinks/8.png|2023/8/14|

#### Sign out page
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|”Sign out”|Go to “Home” page|Click on “Sign out”|
Redirected to ”Log out”|Redirected to “Sign out”|pass|[image](./media/manual-tests/Signout/1.png)|2023/8/14|

#### Burger Menu for screen sizes below 700px

Conduct test no. 9 & 10 without any actions in between*
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Burger menu| set the window size to 690px | click the burger menu | the Menu box opens |the Menu box opens| pass|[image](./media/manual-tests/BurgerMenu/1.png)|2023/8/14|
|2|Burger menu| --| click the burger menu for the second time | the Menu box closes |the Menu box closes| pass|[image](./media/manual-tests/BurgerMenu/2.png)|2023/8/14|
|3|Burger menu| --| click the burger menu to open the menu. Click outside the menu box. | The Menu box closes |The Menu box closes| pass|[image](./media/manual-tests/BurgerMenu/3.png)|2023/8/14|

#### Footer
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link to facebook|Go to “Home” page|Click on the facebook icon|Redirected to facebook site|Redirected to facebook site| pass|[image](./media/manual-tests/Footer/1.png)|2023/8/14|
|2|link to twitter|Go to “Home” page|Click on the twitter icon|Redirected to twitter site|Redirected to twitter site| pass|[image](./media/manual-tests/Footer/2.png)|2023/8/14|
|3|link to instagram|Go to “Home” page|Click on the instagram icon|Redirected to instagram site|Redirected to instagram site| pass|[image](./media/manual-tests/Footer/3.png)|2023/8/14|

#### The flash messages
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1| setTimeout function in line 2-6 of script.js | log out | log in as testuser | Redirected to the home page.  The message "Successfully signed in as testuser" will show up and disappear after 5 seconds. |Redirected to the home page.  The message "Successfully signed in as testuser" shows up and disappears after 5 seconds.| pass|[image](./media/manual-tests/FlashMessages/1.png)2023/8/14|

*Here I test only that the message is displayed for 5 seconds.  The contents of the messages were tested in the automated tests.*

#### Home
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link ”become a member” in the introduction |--|Click the link|Redirected to "Become a member."| Redirected to "Become a member."|pass|[image](./media/manual-tests/Home/1.png)|2023/8/14|
|2|link ”Read the full story” at the bottom of "blog 3" |--|Click the link|Detail page of "blog 3" will be displayed.| Detail page of "blog 3" is displayed.|pass|[image](./media/manual-tests/Home/2.png)|2023/8/14|
|3|link ”Read the full story” at the bottom of "blog 2" |--|Click the link|Detail page of "blog 2" will be displayed.| Detail page of "blog2" is displayed.|pass|[image](./media/manual-tests/Home/3.png)|2023/8/14|
|4|link ”Read the full story” at the bottom of "blog1" |--|Click the link|Detail page of "blog 1" will be displayed.| Detail page of "blog 1" is displayed.|pass|[image](./media/manual-tests/Home/4.png)|2023/8/14|
|5|link ”More stories from this week” |--|Click the link|Redirected to “More stories from this week”| Redirected to “More stories from this week”|pass|[image](./media/manual-tests/Home/5.png)|2023/8/14|
|6|link ”Readers’ favorite stories of all time” |--|Click the link|Redirected to ”Readers’ favorite stories of all time” |Redirected to ”Readers’ favorite stories of all time”|pass|[image](./media/manual-tests/Home/6.png)|2023/8/14|


update comment cancel --> will not be updated