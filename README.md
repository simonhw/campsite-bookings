# Lakeview Campsite

This responsive website is designed to be viewed on a variety of screen sizes. Its purpose is to allow a visiting user to view information about and make a booking to stay at a campsite, and to allow an administrator to view all bookings and related information.

Deployed program on Heroku: [Lakeview Campsite](https://lakeview-campsite-8b683b53a1cd.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/simonhw/campsite-bookings)
![GitHub contributors](https://img.shields.io/github/contributors/simonhw/campsite-bookings)

## Contents
- [User Experience](#user-experience)
    - [Initial Discussion](#initial-discussion)
    - [Agile Planning](#project-planning-with-the-agile-approach)
- [Design](#design)
- [Features](#features)
    - [Features to be Implemented](#features-to-be-implemented)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries, and Programs](#frameworks-libraries-and-programs)
    - [Dependencies](#dependencies)
- [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Live Deployment](#live-deployment)
- [Testing](#testing)
- [Credits](#credits)
    - [Media](#media)
    - [Code Used](#code-used)
- [Acknowledgements](#acknowledgements)


## User Experience
### Initial Discussion
The Lakeview Campsite website facilitates bookings for small and large groups for one night or more of camping. The goal of the site is to encourage business by showcasing the campsite information and offering a user-friendly booking system to users. The website allows staff users to manage all bookings.

### Project Planning with the Agile Approach
The Lakeview Campsite project was built using the Agile method. This involves breaking projects down into smaller manageable sections which allows team to deliver continuous working releases to the client and end users. These release periods are known as sprints and this project had four sprints over nine weeks.

User Stories were generated and grouped under different Epics to effectively structure the work involved at different stages of the project. These Epics were:
- "Initial Project Setup"
- "Create Models"
- "User Accounts"
- "Bookings System"
- "Website Content"
- "Bugs"
- "Documentation"

Each user story was assigned a number of labels to aid in the project workflow. These include:

- `Sprint 1/2/3/4` - To denote in which sprint the user story will be worked on.
- `Story Points: 1/2/3/5/8` - To denote how much effort each user story requires.
- `Must-Have` - A user story relating to a feature without which the website will not function correctly.
- `Should-Have` - A user story relating to a feature that will complement the core website features and enhance the user experience.
- `Could-Have` - A user story relating to a feature which would be of benefit to the user but without which the site will still achieve all its design goals.
- `Site User` - A user story from the perspective of a regular site user.
- `Site Admin` - A user story from the perspective of a site administrator.

Using the Agile method allowed this project to be managed well in small chunks. The developer was able to work on specific tasks without losing focus and manage and project the time required for these tasks optimally.

## Design
### Colour Scheme
A palette of green colours was chosen to reflect the calming and relaxing environment of the campsite, being surround by greenery and nature away from the hustle and bustle of the cities.

![Coolors colour palette](static/images/readme/campsite-colours-v1.png)

### Typography
The Sedan font was chosen from the Google Fonts library because it evoked feelings of a professional but fun business.

![Sedan Font](static/images/readme/sedan-font.png)


### Imagery
Images were chosen that show an attractive campsite and surroundings. Bright images showing tents near a lake and other forms of accommodation were selected to give a sense of an inclusive type of campsite. Images of people helping each other set up a tent were used for the "Need a Hand?" part of the About page. A beautiful drone/helicopter shot of a lake shore with a green landscape and mountains in the background was used in the index and About page to entice site users wishing to escape into nature for a relaxing holiday. 

The hero image for smaller screens was either a tent and chair by the lake's edge or a closeup of books, a mug, and flask, and a camera on the floor of a tent. The latter was used mainly for account pages and the Manage Bookings page to reflect their administrative nature. A wider image of the chair and tent was used for larger screens to make good use of the extra horizontal space.

For the 404, 403, and 500 error pages, two different images were used. For the 403 page an image of a diamond mesh fence was used to convey the sense of forbidden access. For the 404 and 500 error pages, an image of a man looking at his phone in the woods was used, to give the sense of being lost or something having gone wrong.

### Wireframes
Wireframes were created in Balsamiq for the initial front-end design of the website. The mobile layout was designed first and the tablet and desktop were adapted from this.

**Home Page**

![Homepage Wireframe - Mobile](static/images/readme/wireframe-mobile-1.png)

![Homepage Wireframe - Tablet](static/images/readme/wireframe-tablet-1.png)

![Homepage Wireframe - Desktop](static/images/readme/wireframe-desktop-1.png)


**Booking Page**

![Booking Wireframe - Mobile](static/images/readme/wireframe-mobile-2.png)

![Booking Wireframe - Tablet](static/images/readme/wireframe-tablet-2.png)

![Booking Wireframe - Desktop](static/images/readme/wireframe-desktop-2.png)

**Reviews Page**

![Reviews Wireframe - Mobile](static/images/readme/wireframe-mobile-3.png)

![Reviews Wireframe - Tablet](static/images/readme/wireframe-tablet-3.png)

![Reviews Wireframe - Desktop](static/images/readme/wireframe-desktop-3.png)

### Entity Relationship Diagrams
An ERD was created to plan out the models that would be created and used in this project.

![ERDs](static/images/readme/erd-v2.png)

## Features
The website was designed to be as simple as possible, with little to no distracting content. A mobile-first design process was undertaken from the start.
The website is comprised of thrfour main pages visible to the site user: a homepage, about page, a booking form page, and a "my bookings" page (when logged in). A page is also visible to staff users once logged in where they can manage all bookings. Additional pages visible to users include: the signup page, login page, logout page, password reset page, 404 error page, 403 error page, and 500 error page.

**All pages on the website have:**
1. A favicon of a tent next to a tree with a cloud.

    ![Camping favicon](static/images/readme/favicon-camping.png)

2. A header with a title and nav bar or menu dropdown for page links

    ![Website Header](static/images/readme/header-nav.png)

    ![Website Header](static/images/readme/header-dd.png)

    The header contains links to the main pages of the website, depending on the login status of the site user. 
    - The website title "Lakeview Campsite" is a link which when clicked will return the user to the `index.html` page.
    - "About" brings the user to the `about.html` page.
    - "Book Now" brings the user to the `bookings.html` page.
    - "Log In" and "Sign Up" will direct the user to the respective account pages of `login.html` and `signup.html`.
    
    When a user is signed in, the header links change.
    - A new link "My Bookings" brings the user to the `user_bookings.html` page.
    - "Log In" and "Sign Up" are hidden and "Log Out" is shown, which will direct the user to the `logout.html` account page.

        ![Website Header when user is logged in](static/images/readme/header-nav-user.png)

        ![Website Header when user is logged in](static/images/readme/header-dd-user.png)

    When a user with staff status is logged in, instead of "My Bookings", a link titled "Manage Bookings" is shown which brings the user to the `manage_bookings.html` page.
    <br>

3. A footer with contact information and social media links

    ![Website Footer](static/images/readme/footer-mob.png)

## Responsiveness
On small screen sizes, namely mobiles, the website is displayed with content in a scrollable single column. This design was chosen as it is a comfortable and familiar experience for mobile users.

On tablet-sized screens, content is display in multiple columns to make user of the larger space. Reviews are now displayed four at a time with the use of previous and next buttons to view the paginated list.

On large screen sizes, multiple columns are again used, with empty space on the outermost columns to focus the user's attention in the middle of the page. This is more aesthetically pleasing than having content spread aross a wide screen.

## CRUD Functionality
A key requirement for this project was for users to be able to create, read, update, and/or delete data from the database as appropriate. User could interact with the database in these ways as follows:

### Create
* Site users and admin users may **create** by creating an account.
* Site users may **create** by creating a booking.
* Site users may **create** by posting reviews on the website after their stay.
* Admin users may **create** by writing responses to reviews.
* Admin users may **create** by adding information about the campsite to the homepage

### Read
* Site users and admin users may **read** by viewing the camping information page and reviews page.
* Site users may **read** by viewing their list of bookings.
* Admin user may **read** by viewing the list of all bookings.

### Update
* Site users may **update** by editing their account details.
* Site users may **update** by amending their booking information.
* Admin user may **update** by amending the camping information page and adding new photos.

### Delete
* Site users may **delete** by deleting their account.
* Site users may **delete** by cancelling their booking.
* Site users may **delete** by removing their reviews if desired.
* Admin users may **delete** by removing information, photos, or reviews.

### Admin View
The bookings are displayed with more details for the admin user without the use of a dropdown.
The wording changes on the booking page when the admin user edits something.

### Features to be Implemented
- occupancy limits per accom type
- images on booking page per type
- add pricing information and page
- upgrade calendar to booking style with available dates
- diasble the form not just the submit button when not signed in
- sort bookings by month for the admin user

## Technologies Used
### Languages
HTML,
CSS,
Python,
and Javascript

Relational database: PostgreSQL.


### Frameworks, Libraries, and Programs
[Django](https://www.djangoproject.com/) - A Python framework used to design the website.

Visual Studio Code and [Gitpod](https://www.gitpod.io/) - The IDEs used to write my code.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store files online.

[ElephantSQL](https://www.elephantsql.com/) - To create and store the database.

[LucidChart](https://lucid.app/) - To creat Entity Relationship Diagrams

[W3Schools.com](https://www.w3schools.com/) and [The Python Library](https://docs.python.org/3/library/) - For researching and learning about Python methods and syntax.

[ScreenToGif](https://www.screentogif.com/) - To create gif files for this README.

Adobe Photoshop 2020 - To pixellate and crop some README images.

[Heroku](https://www.heroku.com/) - To host the deployed version of the program.

[Shields.io](https://shields.io/) - To add badges to this README.

[CI Python Linter](https://pep8ci.herokuapp.com/#) - To ensure code meets minimum PEP8 standards.

### Dependencies

## Deployment
The program was deployed on Heroku to allow the CI assessor and other interested parties to view and interact with the program.

### Local Deployment
To deploy this program locally on your device, please follow the steps below:

#### Forking
1. Log in or sign up to GitHub.
2. Navigate to the repository for [Scout Waiting List](https://github.com/simonhw/campsite-bookings).
3. Click the Fork button located in the top right part of the webpage.

#### Cloning
1. Log in or sign up to GitHub.
2. Navigate to the repository for [Scout Waiting List](https://github.com/simonhw/campsite-bookings).
3. Click on the green Code button, select your preferred option of HTTPS, SSH, or GitHub CLI, and copy the relevant link.
4. Open the terminal in your IDE and navigate to your directory of choice for this new clone.
5. Type `git clone` into the terminal and paste in your copied link. Press enter.

### Live Deployment

#### Heroku

## Testing
All documentation on the testing of this application can be found in the [TESTING.md](/TESTING.md) file.

## Credits

### Content
Some text content for this fictional website was generate using ChatGPT.
https://chatgpt.com/share/aa45f534-dbd4-484e-a73b-31742d06ca5c
### Media

https://www.pexels.com/photo/camping-chair-near-table-on-river-shore-6271625/
https://www.pexels.com/photo/camping-chairs-and-tent-near-calm-lake-6271654/
https://www.pexels.com/photo/tent-and-portable-chair-on-river-shore-in-summer-6271612/
https://www.pexels.com/photo/brown-wooden-table-under-a-tent-4994126/
https://www.pexels.com/photo/cheerful-traveling-couple-with-tent-near-lake-6271557/
https://www.pexels.com/photo/white-tents-in-the-middle-of-the-woods-4993954/
https://www.pexels.com/photo/tent-on-roof-of-car-on-lakeside-6271725/
https://www.pexels.com/photo/thermos-books-and-photo-camera-on-camp-tent-6271651/
https://www.pexels.com/photo/tent-and-camping-chair-on-river-shore-in-summer-6271619/
https://www.pexels.com/photo/man-in-green-sweater-lost-in-forest-using-smartphone-10374361/
https://www.pexels.com/photo/close-up-photo-of-chain-link-fence-3605822/
https://www.pexels.com/photo/people-sitting-around-bonfire-during-nighttime-4994136/
https://www.pexels.com/photo/autumn-forest-over-lake-in-canada-20843515/
https://www.pexels.com/photo/person-sitting-on-grass-field-facing-on-body-of-water-2516423/
https://www.pexels.com/photo/a-luxurious-tent-on-a-campsite-in-a-forest-5364965/
https://www.pexels.com/photo/tent-on-lake-shore-against-lush-trees-6271631/
https://www.pexels.com/photo/white-and-gray-camper-trailer-7967392/
https://www.pexels.com/photo/chairs-outside-a-tent-6271635/
https://www.pexels.com/photo/lakeshore-and-village-on-plains-17891215/ 

### Code Used
**All code in this project was written entirely by Simon Henleywillis unless otherwise specified below.**
form cleaning 
https://docs.djangoproject.com/en/5.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other 

login/logout redirect
https://stackoverflow.com/questions/806835/django-redirect-to-previous-page-after-login

securing my-bookings/ against non-login users
https://stackoverflow.com/questions/24619629/django-do-not-allow-users-to-see-pages-when-they-are-not-logged-in

editing a django form
https://www.pythontutorial.net/django-tutorial/django-edit-form/ 

solving departure date bug
https://stackoverflow.com/questions/563406/how-to-add-days-to-date 

check superuser for view
https://stackoverflow.com/questions/12003736/django-login-required-decorator-for-a-superuser 

star ratings
https://www.w3schools.com/howto/howto_css_star_rating.asp

## Acknowledgements
- [Creating Your First README - Kera Cudmore](https://github.com/kera-cudmore/readme-examples)
- Graeme
- Robin

## Mentor Meeting Notes
- linter
- w3c
- lighthouse
- extensive testing
- detailed explanation of features and reasons why
- update ERD