# Project 5 - IssueTrack
 See it live on [heroku](https://unicorn-attractor-v1.herokuapp.com/)
## Description

This website is an issue tracker for the imaginary Unicorn Attractor app.

Users can register and submit posts that are either bug reports or feature requests. Then the community can upvote an issue if they feel the bug/feature needs addressing. Upvoting bug reports is free, whereas the user is required to pay for upvoting a feature request. 

## Features

This app offers users the following functionality:

- registration and login 
- viewing user profiles
- issues statistics
- posting and upvoting issue
- commenting on an issue
- buying feature upvotes and checking out.


## Future features

- uploading own avatars for registered users
- more detailed statistics 
- make upvoting use ajax to avoid refreshing the page
- give users the ability to tag their issue with a few keywords
- keyword search / tags support
- Personalized view for registered users (can opt not to display issues with certain tags)

## Testing

Registration
- Tested with abnormal characters and spaces in username - the form is getting rejected as expected
- Any fields left blank are being pointed out to the user and do not allow form submission
- Different passwords are being properly rejected

Creating new issues
- Any fields left blank do not allow for form submission
- User has proper selection of possible issue types: Bug Report or Feature Request

Statistics
- Numbers seem to be properly represented in both 'last week' and 'last month' graphs
- Issues that have 'in progress' status are properly listed on the same page

Upvoting
- Issues that are bug reports are being correctly upvoted and the user is returned to the issue details page.
- Issues that are feature requests are being added to cart
- User is unable to upvote the same issue multiple times, as expected

Checkout
- The user is able to checkout using dummy credit card details:
    card no: 4242424242424242
    cvv: 123
    expiration date: anywhere in the future
- upon succesfully checking out, the upvotes are being correctly assigned to corresponding issues

Technologies used
- Python/Django
- JQUERY/AJAX
- [Chart.js](https://www.chartjs.org)

Credits
- I received inspiration for this app from Codeinstitute's final project outline
