# Campsite Bookings - Testing

Deployed program on Heroku: [Campsite Bookings](https://lakeview-campsite-8b683b53a1cd.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/simonhw/campsite-bookings)
![GitHub contributors](https://img.shields.io/github/contributors/simonhw/campsite-bookings)

## Contents
- [Form Validation](#form-validation)
    - [Accomodation Type](#accommodation-type)
    - [Booking Dates](#booking-dates)
    - [Guest Numbers](#guest-numbers)
    - [Terms and Conditions](#terms-and-conditions)
    - [Form Submission](#form-submission)
    - [Viewing Bookings](#viewing-bookings)
    - [Changing Bookings](#changing-bookings)
    - [Deleting Bookings](#deleting-bookings)
    - [Accounts Pages](#accounts-pages)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Full Testing](#full-testing)
    - [Automated Testing](#automated-testing)
- [Bugs](#bugs)
    - [Known Bugs](#known-bugs)
    - [Solved Bugs](#solved-bugs)

## Form Validation
Validating the data to be submitted by the user is done both on the back and front end. 

### Accommodation Type
The dropdown list of four accommodation types is pre-selected to "Tent" and it is impossible to unselect any option in the list. This value is set in the `models.py` file.

![Accommodation dropdown validation](static/images/readme/dd-val.gif)

```
    accommodation = models.IntegerField(choices=ACCOMMODATION, default=0)
```

### Booking Dates
The minimum values of the arrival and departure dates are set in the `forms.py` file:
        
```
widgets = {
    'arrival': DateInput(attrs={
        'type': 'date',
        'id': 'arrival',
        'min': date.today() + timedelta(days=1)
        }),
    'departure': DateInput(attrs={
        'type': 'date',
        'id': 'departure',
        'min': date.today() + timedelta(days=2)
        }),
}
```

They are set such that the minimum value of arrival is always tomorrow from the point of view of the user, and the departure date is always at least the day after tomorrow.
In most cases the arrival date will be selected first, so the minimum departure must be updated dynamically. this was achieved using [custom JavaScript code](static/js/booking.js). The custom code adds an event listener to the arrival input field and when the value is changed, set the new minimum departure date to be one day after the chosen arrival date.

In cases where the user has selected a departure date and then updates the arrival date to be equal to or after the departure, the form is prevented from being submitted and the user is informed of their error.

![Same date validation](static/images/readme/same-date.png)
![Future arrival validation](static/images/readme/future-date.png)

### Guest Numbers
If users attempt to submit the form with values less than the minimum or greater than the maximum values for the adults and children fields, the form does not submit and the user is informed of their error.

![Minimuim adults validation](static/images/readme/adults-validation.png)
![Minimum children validation](static/images/readme/children-validation.png)

![Maximum adults and children validation](static/images/readme/adult-children-validation.png)

These limits are set in `booking/models.py` using Django core validator classes as shown below:

```
adults = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
children = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
```

### Terms and Conditions
If the user does tick the radio button, the form is prevented from being submitted and a message is displayed reminding the user that they must accept the Terms and Conditions to proceed with the booking.

![Terms and Conditions error message](static/images/readme/tac-error.png)

### Form Submission
When the submit button is clicked on the booking form, the view checks that the requested method is POST and then that the form data is valid. 
```
if request.method == 'POST':
    booking_form = BookingForm(data=request.POST)
```

Passing these checks, the data is saved to the database. If the data is found to be invalid, the page is re-rendered with the data pre-filled in the form, and any error or validation messages are displayed to the user.

### Viewing Bookings
When a user click the "My Bookings" nav bar link, they are brought to the `user_bookings.html` page. This page calls a view that is dependent on the user viewing the page. The queryset of bookings displayed is filtered based on the model's `booked_by` field matching the requesting user.

```
queryset = Booking.objects.all().order_by('-arrival').filter(booked_by=self.request.user)
```

In this way, it is impossible for one user to access another user's booking details even though the page url is the same.

### Changing Bookings
The Edit button is rendered differently on the frontend based on whether the booking is withing the next 48 hours. If is is, the button displayed links to a modal on the page instead of the `edit/` url. The Manage button does not have this limitation. In either case, when a user clicks the Edit or Manage button for a given booking, their identity is verified in the `booking_edit` view. The login_required decorator redirects them to the login url if they are not signed in. This is a backup security check as the user should only be able to view this page after they have logged in.

```
if booking.booked_by == request.user or request.user.is_staff:
```

If this check passes, another if statement checks that requested method is GET. Validating to True, the form is filled with the booking data and the page is rendered.
If the requested method is POST, the booking model is populated with the amended data and is verified using the `is_valid()` method before being saved to the database. If the data is invalid, a HttpsResponseBadRequest is returned and the form is not submitted.

If the if statement above validates to False, a PermissionDenied exception is raised.

### Deleting Bookings
When a user clicks the Delete button for a given booking, their identity is verified in the `booking_delete` view. The login_required decorator is also included before this view to carry the same purpose as described above. If the identity checks pass, a second check takes places to verify the user's identity in conjunction with the `is_within_48h()` method. This ensures that the user receives the correct permissions to edit the details, i.e. the booking owner cannot delete a booking within 48 hours of arrival but a staff user can.

```
if booking.booked_by == request.user or request.user.is_staff:
    if ( booking.booked_by == request.user and not booking.is_within_48h() ) or request.user.is_staff :
        booking.delete()
```

If these conditions are satisfied, the booking is deleted from the database and the user is redirected to either `user_bookings.html` or `manage_booking.html` as shown below:

```
if request.user.is_staff:
    return redirect ('manage_bookings')
else:
    return redirect('user_bookings')
```

### Accounts Pages
The sign in, sign out, sign up, and reset password pages already come with form validation in the Django package. Full testing of these pages is detailed below in [Manual Testing](#manual-testing).

## Testing

### Manual Testing
**User Stories** | **Achieved By:** | **Supporting Images**
--- | --- | ---
**Initial Project Setup** | | 
Set Up Django Files | Installing the correct version of Django in the IDE. Creating a project named "lakeview". Creating an app called "home" and writing a basic view to display "Hello World!" on the homepage. | [Closed Issue on kanban board](static/images/readme/kanban-setup.png)
Create PostgreSQL Database | Creating an ElephantSQL account and generating a new database instance. Add the correct values to the settings file and creating the env.py file. Installing the relevant packages to faciliate databse connection and running migrations. |  [Closed Issue on kanban board](static/images/readme/kanban-create.png)
Deploy Project to Heroku | Creating a new Heroku app and updating the code with gunicorn before deploying the branch. |  [Closed Issue on kanban board](static/images/readme/kanban-deploy-heroku.png)
Deploy Heroku App with Static Files | Setting up the WhiteNoise module and updating the settings file with the relevant information. Creating a staticfiles directory and running the `collectstatic` command. Deploing a new branch on Heroku and verifying all styling is applied. |  [Closed Issue on kanban board](static/images/readme/kanban-deploy-static.png)
**Create Models** | | 
Create Bookings Model | Creating a booking app in Django and a model file with the necessary imports. Creating the model itself with all the appropriate fields shown in the ERD. | [Closed Issue on kanban board](static/images/readme/kanban-create-model.png) 
Move Booking Model to the Correct App | Create a new model in the correct app and changing all referneces in other files to this new model. Running migrations and checking for errors before deleting the old model. |  [Closed Issue on kanban board](static/images/readme/kanban-move-model.png)
**User Accounts** | | 
Create an Account | Clicking the Sign In button and registering personal details in the form. Submitting the form with valid data. | [1. Sign Up Page (top)](static/images/readme/signup-1.png) [2. Sign Up Page (bottom)](static/images/readme/signup-2.png)
**Website Content** | | 
Create Base Template | Creating a base.html file with the common code that will be used across all webpages such as the style links, header, and footer. |  [Closed Issue on kanban board](static/images/readme/kanban-base.png)
View Campsite Information | Navigating to the About page and viewing the content displayed there. |  [1. Website Header (mobile)](static/images/readme/header-dd-user.png) [2. Website Header (dekstop)](static/images/readme/header-nav-user.png) [3. Website Footer](static/images/readme/footer-mob.png)
Create Error Pages | Creating a 404.htmt, 403.html, and 500.html page and storing them in the same directory as base.html |  [1. 404 Error Page](static/images/readme/error404.png) [2. 403 Error Page](static/images/readme/error403.png) [3. 500 Error Page](static/images/readme/error500.png)
**Bookings System** | | 
Make a Booking | Navigating to the Bookings page and selecting an accomodation option, booking dates, and number of guests. |  [Booking Form Page](static/images/readme/booking-form.png)
View My Bookings | Navigating to the My Bookings page and viewing the list of displayed upcoming and past booking. Clicking the link in each booking to view more details. |  [1. My Bookings Page](static/images/readme/my-bookings.png) [2. More details on Bookings Page](static/images/readme/my-booking-details.png)
Edit a Booking | Selecting a valid booking to edit and amending the details in the form provided. |  [Editing a Booking](static/images/readme/edit-booking.png)
Delete a Booking | Selecting a valid booking to delete and confirming the action in the provided modal message. |  [Deleting a Booking](static/images/readme/delete-booking.png)
View All Bookings | Navigating to the Manage Bookings page when logged in with a staff account and viewing the list of all bookings. |  [1. Managing Bookings (top)](static/images/readme/manage-bookings.png) [2. Managing Bookings (bottom)](static/images/readme/manage-bookings-2.png)
**Bugs** | | 
Detail and Keep Track of Bugs | Utilising the Kanban board to track bugs and the actions taken to attempt to solve the issues. |  [Kanban Board view of Bugs](static/images/readme/kanban-bugs.png)

### Full Testing
The program was deployed on Heroku and tested there on a Windows 10 desktop with a 26" monitor and on a One Plus 9 Pro mobile phone.

The site was tested on Google Chrome on desktop, and DuckDuckGo on mobile.

| Feature | Expected Outcome | Test Performed | Results | Test Status |
| --- | --- | --- | --- | --- | 

### Automated Testing

## Bugs
### Known Bugs
| # | Bug | Image | Plan to Solve |
| --- | --- | --- | --- |
| 1 | On some mobile screen sizes, the signup form fields are not visually consistent. Some are inline with their labels while others are on a new line. | ![Image of Unsolved Bug #1](static/images/readme/bugs/ubug-01-signup-fields.png) | Writing a custom form for the signup page will allow for more customisation and control. This will be implemented in a future version of the website. |

### Solved Bugs
| # | Bug | Image | Solution |
| --- | --- | --- | --- |
| 1 | When initially deployed to Heroku, the app did not run. | ![Image of Bug #1](static/images/readme/bugs/bug-01.png) | The full logs showed that there was a `H10` error which allowed me to find a solution in a thread on Slack. The issue was caused by not adding the `DATABASE_URL` and `SECRET_KEY` values to the config vars in Heroku. |
| 2 | When creating a booking, the accommodation options were not being accepted by the system. | ![Image of Bug #2](static/images/readme/bugs/bug-02.png) | The error was discovered to be an incorrect field being used in the models.py file: `accomodation = models.TextField(choices=ACCOMODATION, default=0)`. The TextField was changed to an IntegerField and the options were then valid in the admin panel. |
| 3 | In the admin panel, when returning a string for the bookings using a method, the integer value of the accommodation field was displayed instead of the desired string value. | ![Image of Bug #3](static/images/readme/bugs/bug-03.png) | The solution to this was found on [Stack Overflow](https://stackoverflow.com/questions/60556709/how-do-i-get-the-string-value-of-the-tuple-in-django) |
| 4 | When applying custom CSS classes to Bootstrap components, the styles were not taking effect and only the Bootstrap defaults were being shown. | ![Image of Bug #4](static/images/readme/bugs/bug-04.png) | This issue was solved by moving my style.css link to be after my Boostrap link in the base.html file. This allowed the custom style to be applied after Bootstrap styles had been called. |
| 5 | When the DateInput widget was included in the BookingForm model, the front-end input did not give any type of date picker interface. The Django docs did not list any other arguments to include to make this work. | ![Image of Bug #5](static/images/readme/bugs/bug-05.png) | A post was found on [Stack Overflow](https://stackoverflow.com/questions/61076688/django-form-dateinput-with-widget-in-update-loosing-the-initial-value) that included attribute values inside the DateInput widget. This allowed the user to select a date from a calendar.  |
| 6 | After adding code to show a success message after a booking is made, no toast appeared on the webpage. | | The necessary HTML code to show a div containing the messages was omitted. After including this code, the messages began displaying correctly. |
| 7 | When declaring `clean` methods inside the form class, the user is able to submit forms regardless of data validation. The method does not seem to be called when `is_valid()` is run. | | The `if` statements were not testing for the right conditions. Using `print` statements, the developer better understood the `POST` process and how the data was handled. The `clean` method was updated to properly validate the data and it then worked as expected. |
| 8 | After logging in or logging out, the user is redirected to the home page instead of the previous page they were viewing. | ![Gif of Bug #8](static/images/readme/bugs/bug-08.gif) | The code `?next={{request.path}}` was appended to each href in the relevant anchor tags throughout the website. |
| 9 | The integer value in the accommodation tuple was displayed in HTML instead of the desired string value. | ![Image of Bug #9](static/images/readme/bugs/bug-09.png) | A new method `string_from_tuple` which uses `dict` and `get` was written to return the string value from the accommodation tuple given a certain integer.  |
| 10 | The base code for the collapse component taken from the Bootstrap documentation did not work when the link or button were clicked. | ![Gif of Bug #10](static/images/readme/bugs/bug-10.gif) | This post on [StackOverflow](https://stackoverflow.com/questions/22955916/bootstrap-collapse-not-collapsing) highlighted a change in the attributes names. For example, `data-toggle` is now `data-bs-toggle` and `data-target` is `data-bs-target` etc. |
| 11 | When the user viewing their bookings clicked on the collapse component for one particular booking, all bookings expanded. | ![Gif of Bug #11](static/images/readme/bugs/bug-11.gif) | The use of `{{ booking.booking_id }}` as the unique collapse ID was correct however it needed to be preprended by the word "collapse" for it to work properly. |
| 12a | When using the DateInput field in the form, the departure date was not being limited as expected and could be assigned a value earlier than the arrival date. | ![Image of Bug #12a](static/images/readme/bugs/bug-12.png) | Using print statements, it was discovered that the date values were being manipulated in a format not acceptable to the DateInput field. It was necessary to refactor the date back into the expected format by getting the year month and day separately. |
| 12b | After solving Bug #12a, the departure date was still not being limited to the correct month. | |  The `getMonth()` method is 0-indexed so the month value needed to be incremented by 1 for the date to be properly restricted, i.e. 0 corresponded to January, 1 to February etc. |
| 13 | The departure date was not always restricted to at least one day after the selected arrival date. | | The new Date variable needed to be instantiated with the arrival date value otherwise it returned erroneous values. The use of `console.log()` statements showing the erroneous values allowed this error to be discovered. |
| 14 | When logged in as a non-superuser, adding any booking ID to the end of .../booking/my-bookings/edit/ allowed the user to view the details and amend the bookings. | ![Image of Bug #14 Solution](static/images/readme/bugs/bug-14.png) | The highlighted code in the image was added to the booking_edit view. This ensured only the authorised user was able to view the details and additionally a PermissionDenied exception was explicitly raised otherwise. |
| 15 | When logging out from the user bookings page, the user is returned to a now empty webpage. | ![Image of Bug #15](static/images/readme/bugs/bug-15.png) | This issue was initially indirectly solved by the addition of backend code that requires a user to be logged in to view this particular page. When a user signed out on this page, they were redirected to the Sign In page by default; however, this was not a very nice user experience, so the sign out links were updated to redirect directly to the home page in all cases. |
| 16 | When attempting to delete a booking from the Manage Booking page, the staff user was shown a 404 error page, whereas the user who owned the booking was able to delete it without issue. | ![Image of Bug #16](static/images/readme/bugs/bug-16.png) | A new url path needed to be defined for the Manage Bookings page. The issue was resolved after updating the app urls. |
| 17 | On one occasion, while testing if a user could view a different user's bookings, the 500 error page was displayed. In this instance, the site menu nav links displayed as if the user was not logged in. | | This bug could not be replicated again. It appears to be have been solved indirectly since it was first noticed or at the very least it occurs intermittently. |
| 18 | Upon attempting to edit a user booking and update the new data as the booking owner, no toast messages was displayed. In fact, the page simply refreshed with the old booking data pre-filled in the form. The staff user was able to edit the booking successfully. | ![Image of Bug #18](static/images/readme/bugs/bug-18.png) | An invalid if statement structure was discovered in the `booking_edit` view. Parentheses were added around the two `request.user` checks so that they worked correctly with the `request.method` check.

<br>

Back to [README.md](/README.md)