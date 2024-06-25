# Campsite Bookings - Testing

Deployed program on Heroku: [Campsite Bookings]()

![GitHub last commit](https://img.shields.io/github/last-commit/simonhw/campsite-bookings)
![GitHub contributors](https://img.shields.io/github/contributors/simonhw/campsite-bookings)

## Contents
- [](#)
    - [](#)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Full Testing](#full-testing)
    - [Automated Testing](#automated-testing)
- [Bugs](#bugs)
    - [Known Bugs](#known-bugs)
    - [Solved Bugs](#solved-bugs)

![API error gif](assets/images/readme/validate-api-error.gif)

### Manual Testing
| User Stories | Achieved by: | Supporting Images |
| --- | --- | --- | 

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

### Solved Bugs
| # | Bug | Image | Solution |
| 1 | When initially deployed to Heroku, the app did not run. | ![Image of Bug #1](static/images/readme/bugs/bug-01.png) | The full logs showed that there was a `H10` error which allowed me to find a solution in a thread on Slack. The issue was caused by not adding the `DATABASE_URL` and `SECRET_KEY` values to the config vars in Heroku. |
| 2 | When creating a booking, the accommodation options were not being accepted by the system. | ![Image of Bug #2](static/images/readme/bugs/bug-02.png) | The error was discovered to be an incorrect field being used in the models.py file: `accomodation = models.TextField(choices=ACCOMODATION, default=0)`. The TextField was changed to an IntegerField and the options were then valid in the admin panel. |

Back to [README.md](/README.md)