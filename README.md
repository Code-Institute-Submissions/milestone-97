# Game review

My project is a video game review site. All of my milestone projects so far have been video game related so i thought best to continue the tradition.
the goal of this site is for users to be able to come to the site and leave a review on any video game that they would like. any user that visits 
this site shpuld be able to read others reviews, post their own, edit their own and delete their own reviews.
 
## UX
### Targeted User
* This website is targeted at gamers that want to either leave reviews on games or read them.
* Ideally People above the age of 18.
* People who love to share their opinion with others.
* people who love to read other peoples opinions.

### User Story
1. As a new user to this Website, I want to easily navigate the website so i can find 
the information i need.
2. As a new user to this Website, I want important information visible to me when i load up the 
website initially.
3. As a new user to this Website, Iwant to be able to imediately read a review.
4. As a new user to this Website, I want to be able to easily register an account.
5. As a new user to this Website, I want to be able to create my own reviews as well as edit
them or delete them. 
6. As a new user to this Website, I want to know the price of the games that are being reviewed.

### Wireframes
My wireframe is stored in my repository in a folder named "wireframe".

## Features
* This is a multi page website
* The page is also reponsive.
* Users are able to register an account on the site.
* Users are able to log in and log out of the site.
* Users are able tpo leave a video game review. 
* It is possible for users to edit and delete their own reviews.

### Features Left to Implement
* A feature I would like to implement in the future would be letting the users choose their own image for on
top of their review or even on their profile page.

## Technologies Used
* This website uses HTML programming language.
* This website uses CSS programming language.
* This website uses Python programming language.
* This website uses JavaScript
* This website uses jQuery
* This website uses a flask Framework
* This website uses MongoDB
* This website uses jinja
* This website uses PyMongo
* This website uses Flask PyMongo
* This website uses materialize CDN. materialize was used to ensure a responsive and consistent 
website.
* This website uses Font Awesome. [https://fontawesome.com/] 
* This website also uses Heroku to publish the site.

## Testing
W3C Markup Validation ans W3C CSS Validation were used to validate the code of the website.
* [https://validator.w3.org/]
* [https://jigsaw.w3.org/css-validator/]


### Testing User Stories
1. As a new user to this Website, I want to easily navigate the website so i can find 
the information i need.
* This Site features a navbar that brings you everywhere on the site.
* Page layout is very simple for a user to understand quickly
* When hovering over any buttons they will change colour to inform the user they are on a button, button 
colour will revert when user not hovering on the button.

2. As a new user to this Website, I want important information visible to me when i load up the 
website initially.
* On page load there is a search bar.
* Reviews from other users are imdediately available to read.

3. As a new user to this Website, I want to be able to imediately read a review.
* On Page load, there is reviews available to the user imediately.

4. As a new user to this Website, I want to be able to easily register an account.
* On the navbar there is a button that brings you the registration page.

5. As a new user to this Website, I want to be able to create my own reviews as well as edit
them or delete them.   
* Once the user is registered they are able to make a review from the button on the navbar, the can then edit their
review after it is published onto the home page.

6. As a new user to this Website, I want to know the price of the games that are being reviewed.
* In each review users are required to provide a price for the video game they are reviewing.

### Manually testing functionality of the website
#### Home Page:
1. Navbar / Sidenav:
* Go to the homepage with a desktop screen size
* Make sure all buttons are showing for when user is not logged in.
* Ensure that all button perform the correct task
* Change screen size from desktop to tablet checking responsiveness of the navbar.
* Change screen size from tablet to mobile and repeat the above step. 
* Repeat these steps again using a mobile device and a tablet.
* Repeat these steps with a logged in user.
* Repeat these steps on every page of the site.

2. Search Bar:
* Go to the homepage with a desktop screen size
* Attempt to search for a review.
* Attempt to reset the page.
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.

3. Reviews:
* Go to the homepage with a desktop screen size
* Ensure name of came is being shown just below its image.
* Ensure the accordian is working when clicked on.
* When accordian is clicked ensure correct content is revealed.
* Change screen size from desktop to tablet to make sure the all content responds properly.
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.


4. Footer:
* Go to the homepage with a desktop screen size
* click on all available links.
* Change screen size from desktop to tablet to make sure the all content responds properly and
that there is no overflow issues with padding or margins.
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.
* Repeat these steps on every page of the site.
 
#### Register Page:
1.Form
* Ensure user can only enter 8-15 characters and alphanumeric character into both
the username and password fields.
* Ensure when wrong characters are entered the form informs the user.
* When user clicks register ensure the correct flash message appears.
* Ensure link below form also works.
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.


#### Log In Page:
1.Form
* Ensure user can only enter 8-15 characters and alphanumeric character into both
the username and password fields.
* Ensure when wrong characters are entered the form informs the user.
* When user clicks Log in ensure the correct flash message appears.
* Ensure button works.
* Ensure link below form also works.
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.

#### New Review Page:
1.Form
* Ensure user has to fill ever part of the form
* Ensure button works.
* When user clicks Log in ensure the correct flash message appears.
* When user clicks Log in ensure user is brought to the correct location.
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.

#### Manage Page:
1.
* Ensure all user reviews are present on the screen.
* Ensure only "theadmin" can arive at this page.
* Ensure all buttons work correctly
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.

#### Edit ReviewPage:
1.
* Ensure user has to fill all parts of the form
* Ensure cancel button returns user to homepage
* Ensure finish edit button actually edits the review
* Ensure only the user who made the review can edit it, besides the admin.
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.

#### 404 Page:
1.
* Ensure when invalid link is searched that user is brought to custom 404 page
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.

### More Testing
1. Asked my family and friends to look at the site to see if they could find any bugs. 
(This happened after I had done all my own testing, no bugs were found by them)

## Deployment

### This project was deployed using Heruko using github repositories
1. Ensure your project dependencies and requirements are included in a requirements.txt file
in your project folder.
2. To complete this you will need to enter the following code into your terminal
"pip3 freeze --local > requirements.txt"
3. Create a Procfile by typing the following command into your terminal
"echo web: python app.py > Procfile"
4. Commit and push these changes to your repository
5. Create and acccount on Heroku 
6. Once logged in select new the create new app.
7. Create a project name that is completely unique and select your region
8. Click on the option that will connect you directly to your github acount
9. Ensure it is your account that is displayed and then search for your project.
10. After this Input all of your config vars in the settings tab.
11. You may now go back to the deploy tab and "Enabe automatic deploy"
12. Then click deploy branch just underneath.
13. Your app shpuld start to build and within a few moments youll be given an 
option to view what you deployed.

### How to run this project locally
You will need a Github account and a browser (chrome)
1. Install the gitpod chrome extension to your browser. 
[https://www.gitpod.io/docs/browser-extension/]
2. After installation, go to github.com and find this project repository.
[https://github.com/Robertl231/milestone-3] 
3. Click on the green "Gitpod Button" in the top right above the repository.
4. Once this is done the site will create a new workspace for this project.


## Credits

### Content
All Content is my own unless stated otherwise here or in the form of comments in the html 
code

* My project was massively helped along by the task manager mini project, I did my best to customise the code so that it
represented me as best as i could. I think I did a good job in making it my own and showing my understanding of the code written. 

### Dificulties I ran into
The biggest difficulty i seem to have is when it comes to indentations, spacings, spelling mistakes or just simply overlooking pieces of code.
I seem to spend hours on the these things and i feel it's something i really need to improve on going forward, im sure with the more i practice the more
it all becomes a force of habit.

### Media
#### The images used in this site were obtained from sources listed below:
1. game-review-hero.png
https://waylandstudentpress.com/94654/ae/video-game-review-hades/

### Acknowledgements

I would like to thank my Mentor Miguel for all his help and guidance, aswell as my friends and family