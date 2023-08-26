# eco post

## CONTENTS

* [Project Goals](#project-goals)
* [User Stories](#user-stories)
* [Features in a Nutshell](#features-in-a-nutshell)
* [Wireframes](#wireframes)
* [Notes on the Design](#notes-on-the-design)
* [Each Part and Function in Detail](#each-part-and-function-in-detail)
* [Deployment Process](#deployment-process)
* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)
* [Bugs](#bugs)
* [Aspects to be improved in the future](#aspects-to-be-improved-in-the-future)
* [Validating python, CSS, Html code with Tools](#validating-python-css-html-code-with-tools)
* [Checking Performance and Accessibility](#checking-performance-and-accessibility)
* [Media](#media)
* [Credits](#credits)
- - -

![ecopost-home](./documents/media/readme/home.png)
<img src="./documents/media/readme/mobile.png" width="250" alt="ecopost displayed on mobile">

The website is deployed [here](https://ecopost.herokuapp.com/).

## Project Goals
eco post offers a platform where users can share their stories on what they are doing to protect the environment. Many people feel helpless, thinking that individuals cannot do so much. Here, visitors can read posts written by others, leave comments and write their own stories. Users can connect with others who are concerned about the environmental crisis, get motivated to take actions, or at least find some hope.  The app can target users in a particular region or a country.

## User Stories

No.|As a… |I can…|so that …|Priority (1 is the highest)|
|:--|:-----|:--------------------------------|:----------------------------------------|:--|
|1|site visitor | understand what the site is for and how to use it| I can immediately start using the site.| 1|
|2|site visitor | use this site on screen of different sizes | I can use the app on any devices.| 1|
|3|site visitor | sign up for an account| I can participate in the community by writing posts and comments|1|
|4| user | see featured posts on the home page |I don't necessarily have to look for what to read but can immediately read interesting posts.| 1|
|5| user | see the detailed page of a post |I can read the full content of the post as well as comments written on the post.| 1|
|6| user |see a list of recently published posts | I can browse through the newest posts.| 1|
|7| user | see a list of most ‘liked’ posts |I can browse through popular posts.| 1|
|8| member | write posts |I can share my stories with other users.| 1|
|9| member | edit my drafts |I can update or correct the content.| 1|
|10| member | delete my posts |writings that I no longer need will be removed from the database.| 1|
|11| member |write comments on posts |I can participate in discussions with other members.| 1|
|12| member | edit my comments |update or correct the content.| 1|
|13| member | delete my comments |take back my comments if I change my mind later.| 1|
|14| user | search posts by title, author, keywords, published dates and other factors | I can find the kind of posts I am looking for.| 1|
|15| member |‘like’ posts | I can show my appreciation for particular posts.| 1|
|16| member| see a page displaying 1. the posts and drafts I've written, 2. the posts I've commented on and 3. the posts I've bookmarked | I can easily access them.| 1|
|17| admin|present posts that are particularly interesting on the home page | visitors are likely to read them first and get a good impression of the site. |1|
|18| admin | make sure that users can update or delete their posts only before they submit their drafts | published posts will not be suddenly changed or get deleted.| 1|
|19| admin| make sure that users can update or delete only the posts and comments written by themselves | the users can be assured that no one else will make changes to their writings.| 1|
|20|admin | make sure that users can access only their own ‘My Page’ | users cannot access pages that are irrelevant to them.| 1|
|21|user|see feedback messages | I can be sure the requests I made have been processed. |1|
|22|user |see a confirmation dialog before deleting my drafts and comments | I will not delete them by mistake.| 1|
|23| user |bookmark posts | I can easily access certain posts later.| 2|

## Features in a Nutshell:
Users can see lists of excerpts from
-	featured stories
-	posts published in the previous 7 days
-	most liked stories of all time
-	posts written by them
-	posts commented by them
-	posts bookmarked by them

Users can read the entire content of published posts<br>
Users can search stories by title, authors and other factors<br>
Users can sign up to become members<br>
Members can like and bookmark posts<br>
Members can leave comments on the posts<br>
Members can write their own stories and publish them<br>
Members can edit and delete comments<br>
Members can update or delete their posts before publishing them<br>

## Wireframes
Wireframes for the app can be found [here.](https://wireframe.cc/pro/pp/873798723651976)
Please click on "Homepage" in the upper left corner to see wireframes of different pages of the app.

## Notes on the Design 
The overall appearance is kept simple and clean so as not to interfere with various colors that the featured images will bring in.

**About the Colors**
- I used beige (rgb(141, 111, 56)) for the navigation links, headings and buttons.
- I used blue (color: rgb(46, 122, 145)) for links in the text.
- I used light grey (#e8e8e8) for the footer.
- Beige and blue were chosen because they are associated with nature.

**About the Fonts**
- Montserrat Alternates was used for headings because it's stylish and visually pleasant when used sparingly.
- For the content Lato is used since it's readable and familiar.

**Logo, Favicon and other graphics**
- I used a clover for the logo and favicon because it’s a widely liked symbol and is associated with good luck and hope, giving a friendly and positive impression. 
- I used a graphic of blue and green earth next to the heading, because this graphic is beautiful and improves the appearance of the page

## Each Part and Function in Detail

### Navigation (common to all pages)
![nav-bar](./documents/media/readme/navbar.png)
- The logo of the website is located on the left side of the navigation bar. 
- On the right side, links to other pages are provided.
- Logged-in users will find links to ‘Home,’ ‘Search,’ ‘Write Stories,’ ‘My Page’ and ‘Sign out.
- Other users will find links to ‘Home,’ ‘Search,’ ‘Become a Member,’ and ‘Sign in.’
- These terms clearly indicate what these linked pages will present.
- Only the content of 'My Page' may not be clear for first-time visitors, but if they navigate to the page, they will see lists of posts that are grouped by labeled categories, so that should become clear. 

### Footer (common to all pages)
- Links to social networks are provided.

### Home Page

**Heading**<br>
<img src="./media/readme/heading.png" alt="heading" width="400px">
- The heading at the center states the title of this website ‘ecopost.’
- A graphic of earth is placed on the right side. 

**Introduction**
- Below the heading an introductory paragraph explains what the site is for and how to use it.
- The paragraph encourages users to take part in the blog. 
- The first sentence addresses the problem that many people share – that they feel helpless, thinking individuals cannot do much to save the environment, and this is meant to establish immediate connection with the site visitors.
- Then the rest of the paragraph offers a possible solution, inviting users to read the posts and connect with others.    
- The paragraph aims to capture readers’ interests and motivates them to participate in this app in a welcoming and concise manner. 

**Featured Stories Section**
- Among the posts that are submitted in the week, admin of the site will choose three ‘featured stories’ that are most likely to capture readers’ interests and will display those posts in this section.  
- The featured image, title, author, published date and the excerpt of each featured story will be shown, so that users can have general ideas of what the posts are about.
- Each excerpt has a link that says ‘Read the full story,’ which will take users to the detail page that shows the full content of the post.
- Presenting a few featured stories on the home page has advantages: it removes from the visitors the stress of having to choose what to read, and it also increases the chance of users liking the site and wanting to revisit it.  

**Links to More Post Articles**
- At the bottom of the page, links to ‘More stories from this week’ and ‘Readers’ favorite stories of all time’ are provided.
- This invites users to explore more post articles.  

### "More Stories from This Week" and Readers' Favorite Stories of All Time"
- 'More Stories from This Week' will show a list of post articles published in the previous 7 days except the featured stories.
- "Readers' Favorite Stories of All Time" shows a list of post articles that are liked more times than other posts.
- I made this page 'Readers' Favorite Stories of All Time' since interesting posts are worth reading regardless to how old they are.
- The admin can set the number of likes above which posts will be included on this page.  They can do so by setting the variable min_num_likes in line 17 of views.py.
- Each page will show 6 posts, and if there are more than 6 posts, the posts will be paginated.

### Detail Page
- The full content of a given post is presented.
- At the top left, the title, author, city and published dates are stated.
- At the top right the featured image is shown.
- The full text of the blog is presented below the title and the image.
- If the post is in ‘draft’ state, and if the user is the author of the post, update and delete buttons are provided below the post content.
- If the post has been published, comments are displayed on the bottom left.
- The comments are listed in the order of oldest to newest so that users can follow the conversation.
- If users are logged in, they will see a comment form on the right side of the comments so they can leave comments.
- For users who haven’t logged in, a note will say ‘Want to leave comments?  Sign in or Become a member,’ which includes links to log-in and sign-up pages.

**Additional Functions on Detail Page**
- By clicking on the heart icon below the featured image, users can 'like' the post, or undo that action.
- Similarly, by clicking on the book icon next to the heart, users can bookmark the post, or undo the action.
- Bookmarked posts can be found on ‘My Page.’ 
- The like function is an important element of this app since it offers opportunities for interaction among users--readers can express their appreciation for the articles, and the authors will be rewarded. 
- The bookmark function is also a useful function because users can make a list of the posts they want to come back to.

### Write Stories
- Here logged-in members can write their own stories they want to share.
- The fields are: title, content, featured image (optional), cateogry (select box) and city
- if no image is uploaded as featured image, a default image will be set for the post.
- Users can click on 'Save' to save drafts so they can edit them later, or click on ’Publish’ to publish the posts.
- Users are warned that if the post includes any inappropriate content, the post will be removed from the site.

### Update Post
- Authors of the posts can update their own drafts before publishing them.
- They can update the post by writing over prepopulated fields or uploading a new image.
- They can click on 'Save', ‘Publish’ or 'Cancel'.

### Delete Post Function (no page)
- Authors of the posts can delete their own drafts before submitting them by clicking 'Delete' button on "Detail Page.'
- A confirmation dialog will ask if users really want to proceed.
- If 'OK' is clicked, the post will be deleted from the database, and the users are redirected to the home page.

### Update and Delete Comment (Delete comment has no page)
- The writer of the comment can update or delete their comment by clicking on the update icon or the trash bin icon right by their comment on 'Detail Page.'
- If edited, the comment will be labeled with a note 'edited.'
- If deleted, a note will say 'Comment deleted' in place of the comment
- I wanted to label edited and delted comments as such, since the comments are records of interaction among users, and it could cause confusion if comments can be updated or deleted without any notes.  

### Search Stories
- Users can search posts by title, author, keywords, published dates, number of likes, cities and categories.
- They can enter one or more fields and click on ‘Search’ to get the search results.
- The search results will be displayed below the search form.
- If no input was made or only spaces are entered, a note will say, 'Please enter at least one field.'
- If no match was found, a note will say, 'No matching results found'

### Notes on Other Pages
- “Become a Member” (sign up page), “sign in” and “sign out” pages were taken from django.allauth.
- The pages were styled with my own css to match other pages.

### Access Control
**By Desgin**
- Only logged in users will find links to ‘Write Stories’ and ‘My Page’ in the navigation bar so other users can’t get to the pages via links.  
- 'Update' and 'Delete' buttons for posts and comments appear only if the user is the writer of the posts or of the comments.  Others can’t get to update pages or delete posts & comments through buttons.
- 'Update' and 'Delete' buttons for posts will appear only if the posts haven't been published.

**LoginRequiredMixin and UserPassestestMixin**
- In order to prevent users from accessing certain functions by entering URLs, LoginRequiredMixin and/or UserPassestestMixin are used.
- ‘Write Stories’ has LoginRequiredMixin, so users who are not logged in will be sent to a 403 error page.
- ‘Update Post,’ ‘Update Comment’ and ‘Delete Comment’ views are controlled by LoginRequiredMixin and UserPassestestMixin, and these check if the user is the writer of the posts or of the comments.  Other users will be sent to a 403 error page.
- Additionally, since posts should not be updated or deleted once published, the program is written to send a 403 page if users attempt to update or delete published. 
- For DeletePosts view function, a program is wrriten to raise 403 error in case users attempt to delete posts improperly.  I first used Mixins, but it caused an error so instead I wrote this program (discussed further in 'Bugs' section).

- - -
## Deployment Process

1. Create an app on Heroku:
- On the dashboard on Heroku, click “New.”
- Click “Create new app”
- Name the app and select the region. 
- Click “Create app”

2. Create a database on ElephantSQL.com:

3. At the top level in the project, make env.py file and write the following:

`import os`<br>

`os.environ[“DATABASE_URL”] = “” // write copied URL from Elphant SQL`<br>
`os.environ[“SECRET_KEY”] = “” // make up a secret key`<br>
`os.environ[“PORT”] = "8000"`<br>
`os.environ[“CLOUDINARY_URL”] = “” // copy and paste the cloudinary url`<br>

4. Save the file, add the file name env.py to .gitignore file so the content won’t be published on Github.

5. In settings.py, add the following:
 
`import os`<br>
`import dj_database_url`<br>
`if os.path.isfile(‘env.py’):`<br>
`    import env`

6. Replace SECRET_KEY as follows:
`SECRET_KEY = os.environ.get(‘SECRET_KEY’)`

7. Add the app’s URL on Heroku as allowed host
`ALLOWED_HOSTS = [‘appname on Heroku’]`

8. Comment out the original DATABASES and add the following:
`DATABASES = {
    ‘default’: dj_database_url.parse(os.environ.get(“DATABASE_URL”))
    }`

9. Make Procfile at the top level and write inside:
`web: gunicorn appname.wsgi`

10. Add the following so the summernote editor will be loaded when deployed.
`X_FRAME_OPTIONS = ‘SAMEORIGIN’`

11. Save, add, commit and push the change.
Then run python3 manage.py migrate to migrate the database structure to the new ElephantSQL database.

12. On Heroku dashboard, select the app, and open the Settings tab.  Add the following config vars:
DATABASE_URL, SECRET_KEY and PORT = 8000

13. Go to “Deploy” tab, in the “Deployment method” section, select “Github.”  Enter the project name in Github and click “connect.”  Scroll down to the bottom of the page and click “Deploy Branch.”

_ _ _
## Automated Testing
Automated tests were written in test_models.py, test_forms.py and test_views.py.
The list of items tested can be found [here](./documents/AUTOMATEDTESTS.md).

## Manual Testing
Manual tests can be found [here](./documents/MANUALTESTS.md)

### Testing User Stories
No. | Goals | How they are achieved | 
|:---| :--- | :--- |  
|1| What the site is for and how to use it are clear. | An introductory paragraph on the home page describes what the site is for and how to use it.  Also the links in the navigation bar indicate which page has which functionality so users can easily understand how to use the app. | 
|2|The app can be used on screen of different sizes|All pages of the app are responsively designed.| 
|3| Visitors can sign up. | Users can go to the sign up page via the link in the navbar, present on all pages.  Also, at the end of the introductory paragraph on the home page, another link to the sing up page is provided. | 
|4| Users can see the detail page of a post. | All post excerpts have a link ‘Read the full story,’ and by clicking the link, users can go to the detail page. The detail page displays the full content of the post and comments written on the post. |
|5| Featured posts are presented on the home page. | Three featured posts chosen by editors are displayed on the home page. |
|6| Users can see a list of recently published posts. |By clicking the link on the home page 'More Stories from this week' users can go to the page displaying a list of recently published posts. | 
|7| Users can see a list of popular posts. | By clicking the link on the home page 'Readers' favorite stories of all time' users can go to the page displaying a list of the posts that have been liked the most. |
|8| Users can write posts. | On ‘Write Stories’ page logged in users can write their own posts and submit them.  The posts will be published if admin of the site approves of them. |
|9| Users can edit posts. | By clicking 'update' on the post_detail page, users can edit their posts. |
|10| Users can delete posts. | By clicking 'delete' on the post_detail page, users can delete their posts.|
|11| Users can write comments. | Logged in users can leave comments on the post_detail page.|
|12| Users can edit comments | By clicking the edit icon, users can delete their comments. |
|13| Users can delete comments. | By clicking the trash bin icon, users can delete their comments. |
|14| Users can search posts. | On "Search Stories" page, users can search posts by multiple factors. |
|15| Users can like posts. |By clicking on the heart icon, logged in users can like posts.|
|16| Users have easy access to the posts written, commented or bookmaked by them. |'My page' displays these three groups of posts.|
|17| The most interesting posts are presented on "Home" |Three featured stories chosen by admin will be displayed on the home page. |
|18| Allow users to update or delete posts only before submission | ‘Update’ and ‘Delete’ buttons for posts appear only if posts are in ‘draft’ status.  In addition, the code is programmed to raise errors if attempts are made to update or delete submitted posts. (line 226 & 232 in views.py) |
|19| Allow only the authors to update/delete the posts & comments | LoginRequiredMixin and UserPassestestMixin allow only the users who are logged in as the authors of posts and comments to update or delete their writings. |
|20|Allow users to access only their own “My page” | LoginRequiredMixin and UserPassestestMixin will allow users to access only their own “My Page.” |
|21|Users get feedback messages|Feedback messages are displayed on the top of the page for 5 seconds after requests from the users have been processed. |
|22|Users will see delete confirmation dialogs. |Before deleting their posts or comments, users will see delete confirmation dialogs. |
|23| Users can bookmark posts. |By clicking the bookmark icon, logged-in users can bookmark posts.  The bookmarked posts will be displayed on 'My Page'. |

#### Testing Features
As preparatory steps,
1. create a user with username "testuser" and a password "gR48NmYr1" (leave the email blank)
2. Sign in as "testuser"
3. make 10 posts with the following field values:
title: blog 1, blog 2, blog 3, blog 4, blog 5, blog 6, blog 7, blog 8, blog 9, blog 10
content: (for all of them): test content
city: Dublin
country: Ireland
4. go to admin panel.
5. publish blog 1-10 one by one in the order.
6. set featured_flag True for blog 1-3.
7. go to "Detail Page" of blog 4-10 and click 'like' button

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image|Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Logo link|Go to “Search Stories”|Click the logo|Redirected to the home page|Redirected to the home page|pass|[image](./media/manual-tests/navlinks/1.png)|2023/8/14|
|2|Link to ”Home”|Go to “Search Stories” page|Click the link “Home”|Redirected to ”Home"|Redirected to ”Home”|pass|[image](./media/manual-tests/navlinks/2.png)|2023/8/14|
|3|Link to ”Search stories”|Go to “Home”|Click “Search Stories”|Redirected to ”Search Stories”|Redirected to ”Search Stories”|pass|[image](./media/manual-tests/navlinks/3.png)|2023/8/14|
|4|”Become a Member”|Go to “Home” page|Click “Become a Member”|Redirected to ”Become a Member” | Redirected to “Become a Member”|pass|[image](./media/manual-tests/navlinks/4.png)|2023/8/14|
|5|”Log in”|Go to “Home” page|Click “Log in”|Redirected to ”Log in”|Redirected to “Log in”|pass|[image](./media/manual-tests/navlinks/5.png)|2023/8/14|
|6|”Write Stories”|Log in and go to “Home”|Click “Write Stories”|Redirected to ”Write Stories”|Redirected to ” Write Stories”|pass|[image](./media/manual-tests/navlinks/6.png)|2023/8/14|
|7|”My Page”|Go to “Home” page|Click “My Page”|Redirected to ”My Page”|Redirected to “My Page”|pass|[image](./media/manual-tests/navlinks/7.png)|2023/8/14|
|8|”Log out”|Go to “Home” page|Click “Log out”|Redirected to ”Log out”|Redirected to “Log out”|pass|[image](./media/manual-tests/navlinks/8.png)|2023/8/14|

#### Burger Menu for screen sizes below 700px
*Conduct test no. 2 & 3 without any actions in between.*
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image|Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Hamburger menu| Set the window size to 690px | Check if the burger menu appears. | The burger menu appears. |The burger menu appears.| pass|[image](./media/manual-tests/burger/1.png)|2023/8/15|
|2|Hamburger menu| --| Click the hamburger menu | The menu box opens |The menu box opens| pass|[image](./media/manual-tests/burger/2.png)|2023/8/15|
|3|Hamburger menu| --| Click the link 'Search Stories' | The menu box closes. Redirected to "Search Stories." |The menu box closes. Redirected to "Search Stories." | pass|[image](./media/manual-tests/burger/3.png)|2023/8/15|
|4|Hamburger menu| --| Click the burger to open the menu. Click again on the burger.| The menu box closes. |The menu box closes. | pass|[image](./media/manual-tests/burger/4.png)|2023/8/15|
|5|Hamburger menu| --| Click the burger to open the menu. Click outside the menu.| The menu box closes. |The menu box closes. | pass|[image](./media/manual-tests/burger/5.png)|2023/8/15|

#### Links in the footer
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image|Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link to facebook|--|Click the facebook icon|Redirected to the facebook site|Redirected to the facebook site| pass|[image](./media/manual-tests/footer/1.png)|2023/8/15|
|2|link to twitter|--|Click the twitter icon|Redirected to the twitter site|Redirected to the twitter site| pass|[image](./media/manual-tests/footer/2.png)|2023/8/15|
|3|link to instagram|--|Click the instagram icon|Redirected to the instagram site|Redirected to the instagram site| pass|[image](./media/manual-tests/footer/3.png)|2023/8/15|

#### The flash messages
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image|Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1| Message disappears after 5 seconds. | sign out | sign in as testuser | Redirected to the home page.  The message "Successfully signed in as testuser" will show up and disappear after 5 seconds. |Redirected to the home page.  The message "Successfully signed in as testuser" shows up and disappears after 5 seconds.| pass|[image](./media/manual-tests/flash_messages/1.png)|2023/8/15|

#### Home
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link ”become a member” in the introduction |--|Click the link|Redirected to "Become a member."| Redirected to "Become a member."|pass|[image](./media/manual-tests/home/1.png)|2023/8/15|
|2|link ”Read the full story” at the bottom of "blog 3" |--|Click the link|Detail page of "blog 3" will be displayed.| Detail page of "blog 3" is displayed.|pass|[image](./media/manual-tests/home/2.png)|2023/8/15|
|3|link ”Read the full story” at the bottom of "blog 2" |--|Click the link|Detail page of "blog 2" will be displayed.| Detail page of "blog2" is displayed.|pass|[image](./media/manual-tests/home/3.png)|2023/8/15|
|4|link ”Read the full story” at the bottom of "blog1" |--|Click the link|Detail page of "blog 1" will be displayed.| Detail page of "blog 1" is displayed.|pass|[image](./media/manual-tests/home/4.png)|2023/8/15|
|5|link ”More stories from this week” |--|Click the link|Redirected to “More stories from this week”| Redirected to “More stories from this week”|pass|[image](./media/manual-tests/home/5.png)|2023/8/15|
|6|link ”Readers’ favorite stories of all time” |--|Click the link|Redirected to ”Readers’ favorite stories of all time” |Redirected to ”Readers’ favorite stories of all time”|pass|[image](./media/manual-tests/home/6.png)|2023/8/15|

#### Detail Page
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link to "Become a Member"|Log out|Click the link on the right side of the comments section|Redirected to "Become a Member" page|Redirected to "Become a Member" page|pass|[image](./media/manual-tests/detail_page/1.png)|2023/8/15|
|2|link to "Sign in"|--|Click the link|Redirected to "Sign in" page|Redirected to "Sign in" page|pass|[image](./media/manual-tests/detail_page/2.png)|2023/8/15|
|3|validation message for comment form| Sign in as testuser and go to "Detail Page" page of "blog 1"| leave the comment field blank, and click 'Submit' | A message says "Please fill out this field"| A message says "Please fill out this field"| pass|[image](./media/manual-tests/detail_page/3.png)|2023/8/15|

#### Update/Delete Comments
As preparation,<br>
- Sign in as testuser and go to "Detail Page" of "blog 1."
- Enter "test comment" in the text box and click 'Submit.'
- Conduct test no. 1-2 consecutively.

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Update comment button|--| Click the update icon next to the comment.|"Update Comment" page will be displayed.|"Update Comment" page is displayed.|pass|[image](./media/manual-tests/detail_page_comments/1.png)|2023/8/15|
|2|Delete comment button|--| Click the trash bin icon next to the comment.|Confirmation dialog "Are you sure you want to delete your comment?" will show up. |Confirmation dialog "Are you sure you want to delete your comment?" shows up. |pass|[image](./media/manual-tests/detail_page_comments/2.png)|2023/8/15|
|3|Confirmation dialog - cancel|--|Click 'Cancel'|The dialog diappears, and "Detail Page" is displayed.|The dialog diappears and "Detail Page" is displayed.|pass|[image](./media/manual-tests/detail_page_comments/3.png)|2023/8/15|
|4|Confirmation dialog - ok|Click the trash bin icon.|Click 'OK' in the dialog.|The dialog disappears. A label says 'Comment deleted' where the comment originally was.|The dialog disappears. A label says 'Comment deleted' where the comment originally was.|pass|[image](./media/manual-tests/detail_page_comments/4.png)|2023/8/15|

#### Confirmation Dialog before Deleting Posts
*Write a story and save. Conduct no. 1-3 without any actions in between.*
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Confirmation dialog |--|Go to the "Detail Page" of the draft, and click "Delete"|Confirmation dialog appears and says "Are you sure you want to delete your post?  You won't be able to retrieve the draft.|Confirmation dialog appears and says "Are you sure you want to delete your post?  You won't be able to retrieve the draft.|pass|[image](./media/manual-tests/detail_page_delete_posts/1.png)|2023/8/15|
|2|Confirmation dialog - cancel|--|Click on 'Cancel'|The dialog diappears, and "Detail Page" remains unchanged.|The dialog diappears and the "Detail Page" remains unchanged.|pass|[image](./media/manual-tests/detail_page_delete_posts/2.png)|2023/8/15|
|3|Confirmation dialog - ok|--|Click on 'Ok'|Redirected to "home." A flash message, "Your draft has been deleted." appears.|Redirected to "home." A flash message, "Your draft has been deleted." appears.|pass|[image](./media/manual-tests/detail_page_delete_posts/3.png)|2023/8/15|

#### Recent Stories
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- | :--- |
|1|pagination|--|Go to "More Stories"| Blog 5-10 are displayed in descending order and blog 4 is displayed on the second page.|Blog 5-10 are displayed in descending order and blog 4 is displayed on the second page.|pass|[image1 ](./media/manual-tests/more_stories/1.png)[image2 ](./media/manual-tests/more_stories/1-2.png)[image3](./media/manual-tests/more_stories/1-3.png)|2023/8/16|
|2|link 'NEXT' if paginated|--|Click ‘NEXT’|The second page is displayed.|The second page is displayed.|pass|[image ](./media/manual-tests/more_stories/2.png)|2023/8/16|
|3|link 'PREV' on the second page|--|Click on PREV|The first page is displayed.|The first page is displayed.|pass|[image ](./media/manual-tests/more_stories/3.png)|2023/8/16|

#### Popular Stories
Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|1|content of the page|--|Go to "Popular Stories"| Blog 5-10 are displayed in descending order and blog 4 is displayed on the second page.|Blog 5-10 are displayed in descending order and blog 4 is displayed on the second page.|pass|[image1 ](./media/manual-tests/more_stories/1.png)[image2 ](./media/manual-tests/more_stories/1-2.png)[image3](./media/manual-tests/more_stories/1-3.png)|2023/8/16|
|2|link 'NEXT' if paginated|--|Click on NEXT|The second page is displayed.|The second page is displayed.|pass|[image ](./media/manual-tests/more_stories/2.png)|2023/8/16|
|3|link 'PREV' on the second page|--|Click on PREV|The first page is displayed.|The first page is displayed.|pass|[image ](./media/manual-tests/more_stories/3.png)|2023/8/16|

#### Write Stories
*Log in as testuser*
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Leave all fields empty| -- | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/write_stories/1.png)|2023/8/16|
|2|Leave all fields empty| -- | click ‘publish’ | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/write_stories/2.png)|2023/8/16|
|3|Leave title empty | Enter 'content' for content, 'test city' for city, select 'Afghanistan' for country | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/write_stories/3.png)|2023/8/16|
|4|Leave title empty | Enter 'content' for content, 'test city' for city, select 'Afghanistan' for country | click ‘publish’ | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass|[image](./media/manual-tests/write_stories/4.png)|2023/8/16|
|5|Leave content empty | Enter 'test title 1' for title, 'test city' for city, select 'Afghanistan' for country | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the content | pass|[image](./media/manual-tests/write_stories/5.png)|2023/8/16|
|6|Leave content empty | Enter 'test title 1' for title, 'test city' for city, select 'Afghanistan' for country | click ‘publish’ | A message says "Please fill out this field" for the content | A message says "Please fill out this field" for the content | pass|[image](./media/manual-tests/write_stories/6.png)|2023/8/16|
|7|Leave city empty | Enter 'test title 1' for title, 'content' for content, select 'Afghanistan' for country | click 'save' | A message says "Please fill out this field" for the city | A message says "Please fill out this field" for the city | pass|[image](./media/manual-tests/write_stories/7.png)|2023/8/16|
|8|Leave city empty | Enter "test title 1" for title, 'content' for content, select 'Afghanistan' for country | click ‘publish’ | A message says "Please fill out this field" for the city | A message says "Please fill out this field" for the city | pass|[image](./media/manual-tests/write_stories/8.png)|2023/8/16|
|9|Select nothing for country | Enter "test title 1" for title, 'content' for content, 'test city' for city | click 'save' | A message says "Please select an item in the list" for the country" | A message says "Please fill out this list" for the country" | pass|[image](./media/manual-tests/write_stories/9.png)|2023/8/16|
|10|Select nothing for country | Enter 'test title 1' for title, 'content' for content, 'test city' for city | click ‘publish’ | A message says "Please select an item in the list" for the country | A message says "Please fill out this list" for the country | pass|[image](./media/manual-tests/write_stories/10.png)|2023/8/16|
|11|enter spaces | enter spaces in 'title,' 'content' and 'city'| click 'save' | A message says "Please fill out this field" for the title | A message says "Please select an item in the list" for the country | fail |[image](./media/manual-tests/write_stories/11.png)|2023/8/16|
|12|enter spaces | enter spaces in 'title,' 'content' and 'city'| click ‘publish | A message says "Please fill out this field" for the title | A message says "Please select an item in the list" for the country | fail |[image](./media/manual-tests/write_stories/12.png)|2023/8/16|
|13|enter spaces | enter spaces in 'title,' 'content,' 'city' and select 'Afghanistan' for country| click 'save' | A message says "Please fill out this field" for the title | A message says "This field is required." appears for title, content and city | fail |[image](./media/manual-tests/write_stories/13.png)|2023/8/16|
|14|enter spaces | enter spaces in 'title,' 'content,' 'city' and select 'Afghanistan' for country (Go on to test no. without any actions.)| click ‘publish’ | A message says "Please fill out this field" for the title | A message says "This field is required." appears for title, content and city | fail |[image](./media/manual-tests/write_stories/14.png)|2023/8/16|

- Tests no. 11-14 failed.  Even though these results turned out to be different from the expectation, a validation message tells users to fill out the field, so the features do not need to be corrected.

#### Search Stories
As preparatory steps, go to admin and change the poems as follows:
Delete all other posts.

title| author | content | city | country | category | published date|
|:---| :--- | :--- |:---| :--- | :--- |:--- |
|blog 1| testuser | protecting animals odd numbers | Dublin | Ireland | protecting animals |2023/8/1|
|blog 2| testuser | protecting aquatic system content  | Dublin | Ireland | protecting aquatic system |2023/8/1|
|blog 3| testuser |protecting soil & trees odd numbers  | Dublin | Ireland | protecting soil & trees content |2023/8/6|
|blog 4| testuser |saving resources content| Freiburg | Germany | saving resources |2023/8/6|
|blog 5| admin |saving resources odd numbers | Freiburg | Germany |saving resources |2023/8/18|
|blog 6| admin |saving resources content | Freiburg | Germany | saving resources |2023/8/18|

Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- | :--- |
|1|search by title|—|enter ‘6’ for title and click ‘search’|’blog 6’ will be displayed.|’blog 6’ is displayed.|Pass|[image](./media/manual-tests/search_stories/2.png)|2023/8/19|
|3|search by author|—|enter ‘admin’ for author and click ‘search’|’blog 6’ will be displayed.|’blog 6’ is displayed.|Pass|[image](./media/manual-tests/search_stories/3.png)|2023/8/19|
|4|search by keyword|—|enter ‘odd numbers’ for keyword and click ‘search’|blog 1, 3, 5 will be displayed.|blog 1, 3, 5 are displayed.|Pass|[image](./media/manual-tests/search_stories/4.png)|2023/8/19|
|5|search by likes count|—|enter ‘1’ for ‘liked more than’ field and click ‘search’|blog 4, 5, 6 will be displayed.|blog 4, 5, 6 are displayed.|Pass|[image](./media/manual-tests/search_stories/5.png)|2023/8/19|
|6|search by published date (start date)|—|enter ‘2023/08/01’ for  the published date (start date) and click ‘search’|All 6 blogs will appear.|All 6 blogs appear.|Pass|[image](./media/manual-tests/search_stories/6.png)|2023/8/19|
|7|search by published date (start date)|—|enter ‘2023/08/02’ for  the published date (start date) and click ‘search’|blog 3-6 will appear.|blog 3-6 appear.|Pass|[image](./media/manual-tests/search_stories/7.png)|2023/8/19|
|8|search by published date (end date)|—|enter ‘2023/08/18’ for  the published date (end date) and click ‘search’|All 6 blogs will appear.|All 6 blogs are displayed.|Pass|[image](./media/manual-tests/search_stories/8.png)|2023/8/19|
|9|search by published date (end date)|—|enter ‘2023/08/17’ for  the published date (end date) and click ‘search’|blog 1-4 will be displayed.|blog 1-4 are displayed.|Pass|[image](./media/manual-tests/search_stories/9.png)|2023/8/19|
|10|search by city|—|enter ‘Dublin’ for  the city and click ‘search’|blog 1-3 will be displayed.|blog 1-3 are displayed.|Pass|[image](./media/manual-tests/search_stories/10.png)|2023/8/19|
|11|search by country|—|enter ‘Germany’ for  the country and click ‘search’|blog 4-6 will be displayed.|blog 4-6 are displayed.|Pass|[image](./media/manual-tests/search_stories/11.png)|2023/8/19|
|12|search by category|—|enter ‘protecting animals’ for  the category and click ‘search’|blog 1 will be displayed.|blog 1 is displayed.|Pass|[image](./media/manual-tests/search_stories/12.png)|2023/8/19|
|**| Test search by multiple factors | ||  |  ||  |  |
|13|search by author & keyword|—|enter ‘admin’ for  the author, enter ‘odd numbers’ for the keyword and click ‘search’|blog 5 will be displayed.|blog 5 is displayed.|Pass|[image](./media/manual-tests/search_stories/13.png)|2023/8/19|
|14|search by likes count & published start date|—|enter ‘1’ for  ‘liked more than’ field, enter ‘2023/08/10’ for the published start date and click ‘search’|blog 5 & 6 will be displayed.|blog 5 & 6 are displayed.|Pass|[image](./media/manual-tests/search_stories/14.png)|2023/8/19|
|15|search by author & keyword & category|—|enter ‘testuser’ for  the author, ‘odd numbers’ for keyword, enter ‘saving resources’ for the category and click ‘search’|A note ’no results’ will be displayed.|Note ‘no results’ is displayed.|Pass|[image](./media/manual-tests/search_stories/15.png)|2023/8/19|
|16|enter spaces and search|—|enter spaces for title, author, keyword and city and click ‘search’|All blogs are displayed.|All blogs are displayed.|Pass|[image](./media/manual-tests/search_stories/16.png)|2023/8/19|
|17|'liked more than' field accepts only a number|—|enter 'a' for 'liked more than' field.|'a' can't be entered. |'a' can't be entered.|Pass|[image](./media/manual-tests/search_stories/17.png)|2023/8/19|

#### Image Transformation
("Write Stories" and "Update Stories")

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|image transformation (code in line 40-45 in blog.models.py)|Go to ‘Write Stories.’ Enter ‘test image transformation’ for title, ‘content’ for content, ‘test’ for city, ‘Afghanistan’ for country, upload ‘test_transformation.jpg,’ and click ‘Save’|Inspect the photo| The photo will be cropped to 510 x 340 px. The photo shows the face and the torso of the person (testing the function “gravity: ‘auto’”)  The file size is significantly reduced.|The photo was cropped to 510 x 340px. The photo shows the face and the torso of the person. The file size was reduced from 1.5MB to 33.0kB.|pass|[image1 ](./media/manual-tests/img_transform/1.png)[image2 ](./media/manual-tests/img_transform/1-2.png)|2023/05/02|

#### Update Stories
As preparation,<br>
1. Sign in as testuser, go to "Write Stories," enter "test title 2" for title, "content" for the content, "test city" for city, select 'Afghanistan' for country.
2. click "Save"
3. go to "My page" and click on the link "Read the full story" of the blog "test title 2"
4. click "Update" 

Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|1|Make all fields empty| delete prepopulated title, content, city and unselect the country | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/update_stories/1.png)|2023/08/16|
|2|Make all fields empty| delete prepopulated title, content, city and unselect the country | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/update_stories/2.png)|2023/08/16|
|3|Make title field empty | delete the title but keep the other fields populated | click 'save' | A message says "Please fill out this field" for the title | The title filed is activated, but no message is displayed.| fail|[image](./media/manual-tests/update_stories/3.png)|2023/08/16|
|4|Make title field empty | delete the title but keep the other fields populated| click 'submit' | A message says "Please fill out this field" for the title | The title filed is activated, but no message is displayed. | fail|[image](./media/manual-tests/update_stories/4.png)|2023/08/16|
|5|Make content field empty | delete the content but keep the other fields populated | click 'save' | A message says "Please fill out this field" for the content | A message says "Please fill out this field" for the content | pass|[image](./media/manual-tests/update_stories/5.png)|2023/08/16|
|6|Make content field empty | delete the content but keep the other fields populated | click 'submit' | A message says "Please fill out this field" for the content | A message says "Please fill out this field" for the content | pass|[image](./media/manual-tests/update_stories/6.png)|2023/08/16|
|7|Make city field empty | delete the city but keep the other fields populated | click 'save' | A message says "Please fill out this field" for city | A message says "Please fill out this field" for city | pass|[image](./media/manual-tests/update_stories/7.png)|2023/08/16|
|8|Make city field empty | delete the city but keep the other fields populated | click 'submit' | A message says "Please fill out this field" for city | A message says "Please fill out this field" for city| pass|[image](./media/manual-tests/update_stories/8.png)|2023/08/16|
|9|Unselect country | unselect the country  | click 'save' | A message tells the country must be selected. | "Please select an item in the list" for the country | pass|[image](./media/manual-tests/update_stories/9.png)|2023/08/16|
|10|Unselect country | unselect the country | click 'submit' | A message telss the country must be selected.| "Please select an item in the list" for the country | pass|[image](./media/manual-tests/update_stories/10.png)|2023/08/16|
|11|enter spaces | enter spaces in the title, content and city fields.  | click 'save' | A message tells the fields must be filled. | Message "This field is required" is displayed for the title, content and city| pass|[image1 ](./media/manual-tests/update_stories/11.png)[image2](./media/manual-tests/update_stories/11-2.png)|2023/08/16|
|12|enter spaces | enter spaces in the title, content and city fields.  | click 'submit' | A message tells the fields must be filled. | Message "This field is required" is displayed for the title, content and city| pass|[image1 ](./media/manual-tests/update_stories/12.png)[image2](./media/manual-tests/update_stories/12-2.png)|2023/08/16|
|13|cancel functionality | change the title and content to 'test title 2 updated' & 'content updated'. Change the country to Aland Islands| click 'cancel' | Redirected to "detail page." And the fields remain unchanged. | Redirected to "detail page." And the fields remain unchanged. | pass|[image1 ](./media/manual-tests/update_stories/13.png)[image2](./media/manual-tests/update_stories/13-2.png)|2023/08/16|

*test no. 3 & 4 failed, and these issues will be discussed later in [Test summary](#test-summary) section.*

#### My Page
To prepare<br>
1. sign up with username testuser3
2. go to "Write Stories" page, and make 4 new posts with the titles: blog 11, blog 12, blog 13, blog 14.
3. go to admin panel and publish the 4 posts one by one in the ascending order.
4. go to detail page of the 4 posts and bookmark them.
5. enter "test comment" as comment in all 4 posts and click "submit"

**"Written by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|The layout|--| Go to "My Page" | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown. | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown.|pass|[image](./media/manual-tests/my_page/1.png)|2023/08/17|
|2|The layout|--| Click "Show more" | blog 11 is displayed below blog 14-12. | blog 11 is displayed below blog 14-12.|pass|[image](./media/manual-tests/my_page/2.png)|2023/08/17|

**"Commented by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|3|The layout|--| Go to "My Page" | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown. | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown.|pass|[image](./media/manual-tests/my_page/3.png)|2023/08/17|
|4|The layout|--| Click "Show more" | blog 11 is displayed below blog 14-12. | blog 11 is displayed below blog 14-12.|pass|[image](./media/manual-tests/my_page/4.png)|2023/08/17|

**"Bookmarked by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|5|The layout|--| Go to "My Page" | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown. | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown.|pass|[image](./media/manual-tests/my_page/5.png)|2023/08/17|
|6|The layout in "Bookmarked by me"|--| Click "Show more" |blog 11 is displayed below blog 14-12. | blog 11 is displayed below blog 14-12.|pass|[image](./media/manual-tests/my_page/6.png)|2023/08/17|

**Show more/less buttons in "Written by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|7|"Show more" button| -- |Click "Show more"| blog 11 will be displayed, and the label of the clicked button will change to "Show less" | blog 11 is displayed, the clicked button says "Show less"|pass|[image](./media/manual-tests/my_page/7.png)|2023/08/17|
|8|"Show less" button (upper) | -- |Click "Show less" | "blog 11" will disappear. The clicked button will say "Show more" |"blog 11" disappears.  The clicked button says "Show more" | pass|[image](./media/manual-tests/my_page/8.png)|2023/08/17|
|9|"Show less" button (lower) | Click on "Show more" |Click on "Show less" | "blog 11" will disappear. The button below 3 posts (blog 12-14) will say "Show more" |"blog 11" disappears.  The button below 3 posts (blog 12-14) says "Show more" |pass|[image](./media/manual-tests/my_page/9.png)|2023/08/17|

**Show more/less buttons in "Commented by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|10|"Show more" button| -- |Click on "Show more"| blog 11 will be displayed, and the label of the clicked button will change to "Show less" | blog 11 is displayed, the clicked button says "Show less"|pass|[image](./media/manual-tests/my_page/10.png)|2023/08/17|
|11|"Show less" button (upper) | -- |Click "Show less" | "blog 11" will disappear. The clicked button will say "Show more" |"blog 11" disappears.  The clicked button says "Show more" | pass|[image](./media/manual-tests/my_page/11.png)|2023/08/17|
|12|"Show less" button (lower) | Click on "Show more" |Click "Show less" | "blog 11" will disappear. The button below 3 posts (blog 12-14) will say "Show more" |"blog 11" disappears.  The button below 3 posts (blog 12-14) says "Show more" |pass|[image](./media/manual-tests/my_page/12.png)|2023/08/17|

**Show more/less buttons in "Bookmarked by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|13|"Show more" button| -- |Click on "Show more"| blog 11 will be displayed, and the label of the clicked button will change to "Show less" | blog 11 is displayed, the clicked button says "Show less"|pass|[image](./media/manual-tests/my_page/13.png)|2023/08/17|
|14|"Show less" button (upper) | -- |Click on "Show less" | "blog 11" will disappear. The clicked button will say "Show more" |"blog 11" disappears.  The clicked button says "Show more" | pass|[image](./media/manual-tests/my_page/14.png)|2023/08/17|
|15|"Show less" button (lower) | Click on "Show more" |Click on "Show less" | "blog 11" will disappear. The button below 3 posts (blog 12-14) will say "Show more" |"blog 11" disappears.  The button below 3 posts (blog 12-14) says "Show more" |pass|[image](./media/manual-tests/my_page/15.png)|2023/08/17|

**Test if clicking "Show more" and "Show less" buttons in different sections will function normally**<br>
Preparation:
1. click "Show more" in "Written by me"
2. click "Show more" in "Commented by me"

Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|16|Show more/less buttons in different sections | -- |Click "Show less" in "Commented by me"| "blog 11" in "Commented by me" will disappear. The button in "Commented by me" will say "Show more" | "blog 11" in "Commented by me" disappears. The button in "Commented by me" section says "Show more" | pass|[image](./media/manual-tests/my_page/16.png)|2023/08/17|

#### Become a Member
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link “sign in” | Go to “Become a Member” page | Click the link where it says "Already have an account.... 'sign in'" | Redirected to the sign in page| Redirected to the sign in page |pass|[image](./media/manual-tests/become_a_member/1.png)|2023/8/19|
|2|leave all fields empty| --|click “Sign up” button|A validation error message says “Please fill out this field for the username field| A validation error message says “Please fill out this field” for the username field |pass|[image](./media/manual-tests/become_a_member/2.png)|2023/8/19|
|3|Leave the second password empty|Enter “testuser1” for the username; “abc@test.com” for the email; “swUf8LcR” for the first password field |click “Sign up” button|A validation error message says “Please fill out this field” for the second password field| A validation error message says “Please fill out this field” for the second password field |pass|[image](./media/manual-tests/become_a_member/3.png)|2023/8/19|
|4|Leave the first password empty|Enter “testuser1” for the username; “abc@test.com” for the email; “swUf8LcR” for the second password field |click “Sign up” button|A validation error message says “Please fill out this field” for the first password field.| A validation error message says “Please fill out this field” for the first password field. |pass|[image](./media/manual-tests/become_a_member/4.png)|2023/8/19|
|5|Leave email empty|Enter “testuser1” for the username; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|Redirected to “Home” page and the message says “Successfully signed in as testuser1” | Redirected to “Home” page and the message says “Successfully signed in as testuser1” |pass|[image](./media/manual-tests/become_a_member/5.png)|2023/8/19|
|6|Leave username empty|Enter “def@test.com” for the email; “swUf8LcR” for the two password fields; |click on “Sign up” button|A validation error message says “Please fill out this field” for the username field| A validation error message says “Please fill out this field” for the username field |pass|2[image](./media/manual-tests/become_a_member/5.png)|2023/8/19|
|7|Use already registered username| Enter “testuser1” for the username; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|A validation message says “A user with that username already exists”| A validation message says “A user with that username already exists”| pass|[image](./media/manual-tests/become_a_member/7.png)|2023/8/19|
|8|Use already registered email| Enter “testuser2” for the username; "test@ecopost.com” for the email; “swUf8LcR” for the two password fields |click “Sign up” button|A validation message says “A user is already registered with this email address.”| A validation message says “A user is already registered with this email address.”| pass|[image](./media/manual-tests/become_a_member/8.png)|2023/8/19|
|9|Use common password| Enter “testuser2” for the username; “def@test.com” for the email; “password” for the two password fields |click “Sign up” button |A validation message says “This password is too common.”| A validation message says “This password is too common.”| pass|[image](./media/manual-tests/become_a_member/9.png)|2023/8/19|
|10|enter two different passwords| Enter “testuser2” for the username; “def@test.com” for the email; “rDw74kRmW” for the first password field; “Adr49PwTeB” for the second password field |click “Sign up” button|A validation message says “You must type the same password each time.”| A validation message says A validation message says “You must type the same password each time.”| pass|[image](./media/manual-tests/become_a_member/10.png)|2023/8/19|
|11|Enter all appropriate data| Enter “testuser2”; “def@test.com” for email; “swUf8LcR” for both password fields| click on“Sign up” button|Redirected to “Home” page, and a message says “Successfully signed in as testuser2” | Redirected to “Home” page, and a message says “Successfully signed in as testuser2”| pass|[image](./media/manual-tests/become_a_member/11.png)|2023/8/19|

#### Sign in
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Enter all appropriate data| Enter “testuser”; “gR48NmYr1” for both password fields| click “Sign in”|Redirected to “Home” page, and a message says “Successfully signed in as testuser” | Redirected to “Home” page, and a message says “Successfully signed in as testuser”| pass|[image](./media/manual-tests/signin/1.png)|2023/8/19|
|2|Leave username empty| Enter “gR48NmYr1” for password| click “Sign in”|A message says "Please fill out this field" for username | A message says "Please fill out this field" for username| pass|[image](./media/manual-tests/signin/2.png)|2023/8/19|
|3|Leave password empty| Enter “testuser” for username| click “Sign in”|A message says "Please fill out this field" for password| A message says "Please fill out this field" for password| pass|[image](./media/manual-tests/signin/3.png)|2023/8/19|
|4|Enter wrong password| Enter “testuser” for username; "wrongpw" for password | click “Sign in”|A message says "username and/or password you specified are not correct" | A message says "username and/or password you specified are not correct" | pass|[image](./media/manual-tests/signin/4.png)|2023/8/19|
|5|Enter wrong username| Enter “nouser” for username; "gR48NmYr1" for password | click “Sign in”|A message says "username and/or password you specified are not correct" | A message says "username and/or password you specified are not correct" | pass|[image](./media/manual-tests/signin/5.png)|2023/8/19|
|6|Remember me function| Enter “testuser” for username; "gR48NmYr1" for password; put a check for "Remember me" and sign in. Sign out and go back to the sign in page| Enter "testuser" for username | The password will be automatically filled out. | The password is not automatically filled out. | fail|[image](./media/manual-tests/signin/6.png)|2023/8/19|

*test no. 6 failed.  This issue will be discussed in [Test summary](#test-summary) section.*

#### Sign out
Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|“Sign out” button|Sign in as "testuser." Click "Sign out" in the navigation bar. |Click "Sign out"|Redirected to "Home" page, and the flash message says, "You have signed out." | Redirected to "Home" page, and the flash message says, "You have signed out." |pass|[image](./media/manual-tests/signout/1.png)|2023/8/19|

### Test summary

The following failed tests need to be discussed.

**Manual tests ‘Update Stories’ section test no. 3 & 4**

When the title field is made empty and ‘Update’ is clicked, a validation message should state the title should be filled out, but no message shows up.  I need to overwrite the customized validation, but I didn’t find the way to do that as of August 19th, 2023.  The form doesn’t get submitted without a title, so this will not cause a serious issue.  I will keep working on the issue.

**Manual tests 'Sign in' section test no. 6**

The check box ‘Remember me’ doesn’t function as expected.  If the checkbox is clicked, the password should be automatically filled out the next time the user enters the username, but when the function was tested, the password remained unfilled.  This doesn't cause a serious problem in the app, but I will try to fix the issue in the future.

- - -
## Bugs

1. For “Update Stories” I was using View class instead of UpdateView class.  When I updated posts, if the post had a featured image originally, and if I updated other fields (but not the image) and saved the change, the image was lost.<br><br>**Solution:** I rewrote “Update Stories” using UpdateView class and the issue was resolved.

2. “Search Stories” page didn’t get displayed.  An error page appeared with the message “Reverse for 'post_detail' with arguments '('',)' not found.”<br><br>**Solution:** I was forgetting a slash at the end of the url in urls.py, so I changed the url from ‘search_story’ to ‘search_story/,’ and the issue was resolved.

3. For "Delete Posts" Page, I first used LoginRequiredMixin and UserPassestestMixin in order to make sure the user is the author of the post and that the post hasn't been submitted. That resulted in an error, since the post was deleted before the test func was run, and the test func couldn't find the post in the database.<br><br>**Solution:** I wrote the program on line 221, 226-227 in views.py to bypass the issue, and now the access control is functioning.

## Aspects to be improved in the future
- Remember me function on “Log in” page needs to be fixed.
- I will make Contact page where users can write and submit messages to admin.
- I also want to simplify the process of updating comments.  Instead of displaying a whole new page of 'Update Comments,' I want to display a small input box on "Detail Page" where the original comment is displayed.

## Validating python, CSS, Html code with Tools

- I validated style.css at jigsaw (https://jigsaw.w3.org/)<br>
I got one error saying ‘Property rotate doesn’t exist.’  But clearly property ‘rotate’ is a widely used property of CSS, and it is functioning in the app, so I left the rule as it is.
- I validated html at https://validator.w3.org<br>
- Errors corrected:
1. Error: Stray start tag footer.<br>
I was putting footer tags outside body tags on base.html.  I corrected it by inserting the footer inside the body tags.
2.  span tags in ul tag in more_stories.html ln 45-55<br>
I replaced ul tag with div tag.

After the above corrections the html validation showed no errors.

## Checking Performance and Accessibility
Performance scored 99% on Sign in page, but on other pages it scored between 52% and 72%, and this aspect needs to be improved in the future.
‘Opportunity’ section of the analysis report stated the score can be improved if initial server response time is reduced.  I will try to optimize the code to prepare pages faster. 

Accessibility scored 91% on Update Comment page.
On all other pages accessibility scored 100%.

On Update Comment page, the report said that the score was lowered because the comment form doesn’t have a label.  I inserted a label tag with 'for' attribute in the update_comment.html, but I still got the same score and a warning that I need a label.  I will try to find out how to solve the issue.

Screenshots of the reports are available [here](./documents/LIGHTHOUSE.md)

## Media

Logo image: clover
https://www.freepik.com/free-photos-vectors/clover-logo

Favicon: Clover
https://icons8.com/icons/set/favicon-clover

Heading image: blue earth
https://www.freepik.com/free-vector/watercolor-background-earth-day-with-natural-elements_1069886.htm#query=earth%20plants%20free&position=24&from_view=search&track=ais

Default featured image
https://www.pexels.com/photo/forest-345522/

## Credits
Many thanks to my mentor Jubril Akolade and tutors at Code Institute for their guidance and dedicated support.<br>

For this application, I used the Code Institute's 'Code Star' project as a starting point.

Code snippets that were taken from 'Code Star' are as follows:

- The code to display 3 excerpts of posts in a row 
`{% if forloop.counter|divisibleby:3 %}`
was used in “More Stories,” “Popular Stories” and “My Page.” 

- The code to paginate post lists was used in “More Stories” (after ln 43) and “Popular Stories” (after ln 41).

- The code to display “Comments” and “Leave Comments” sections was used on “Detail Page.”

- The code to display the heart icon and the number of likes was used in “More Stories,” “Popular Stories” and “Detail Page”

- The code to ‘like’ posts was used in line 71-73, 102-104 in “PostDetail” view in views.py.
The same program was also used for ‘bookmark’ function in line 74-76, 105-107 in “PostDetail” view in views.py.

- The code to post comments was used in line 108-117 in PostLikeView in views.py

Other sources for code snippets taken in this project:
- The code to display links to social networks (lines in 68-87 in base.html) was taken from “Love Running” project.

- The code for turning the navbar to a hamburger menu (lines 9-19 in script.js & lines 21-45 in base.html) was taken from [this site.](https://stackoverflow.com/questions/70370519/how-can-i-turn-my-navbar-into-hamburger-menu-for-mobile-using-responsive-design)

- For the code for search system, I took basic ideas from this [youtube video](https://www.youtube.com/watch?v=G-Rct7Na0UQ)

- The code to sign in a testuser (line 16-20 in test_views.py) was taken from [this site](https://stackoverflow.com/questions/2619102/djangos-self-client-login-does-not-work-in-unit-tests)

- The code to handle 500 error was taken from [this site](https://pythoncircle.com/post/40/designing-custom-404-and-500-error-pages-in-django/).
