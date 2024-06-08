# Postmortem — Alx System Engineering DevOps
0x19. Postmortem


``DevOps``
``SysAdmin``

## Postmortem
Before we dive into our postmortem, let's get an overview of the affected application. The app, called AMS, was one of my first freelance projects. I built it for a charity to manage their donors, beneficiaries, and transactions. I used Laravel 5.5 for the back end and MySQL for the database.

## Issue Summary
On May 11th, 2022, a company agent reported that sometimes when they saved new data to the app, the data was added twice. Fortunately, the app was only used internally by company employees and not available to the public. However, the issue impacted the employees' experience and required them to do extra work by deleting the duplicate entries. After investigating the issue, debugging various parts of the application, and testing it in a local environment, I discovered that the root cause was a JavaScript snippet that didn’t work as expected. Its job was to make the submit button unavailable after the first click to prevent the form from being submitted twice.
The problem was resolved within 4 hours after being reported. and the service outage lasted only 20 minutes.

## Timeline (all times GMT)
May 11th, 2022 | 7:00 AM | Issue reported
May 11th, 2022 | 7:20 AM | Investigating the issue
May 11th, 2022 | 10:30 AM | Root cause found
May 11th, 2022 | 11:00 AM | Outage begins
May 11th, 2022 | 11:00 AM | Deploy new code
May 11th, 2022 | 11:20 AM | Application up and running

## Root cause
The issue was caused by a JavaScript snippet designed to disable the submit button upon the first click to prevent duplicate submissions. However, due to a race condition or user actions (e.g., double-clicking quickly or slow internet), the script failed to execute correctly, allowing the form to be submitted multiple times, leading to duplicate entries.
The problem was fixed by updating the JavaScript to ensure the submit button is immediately and reliably disabled upon the first click and adding a server-side check to prevent duplicate data entries.

## Corrective and preventative measures

### Code Correction
- **Fix the JavaScript Snippet**: Correct the script to ensure the submit button is reliably disabled immediately upon the first click.
- **Server-Side Validation**: Add logic on the server to check for duplicate submissions by comparing timestamps and content, rejecting duplicates before saving.

### User Experience Enhancements
Modify the button to provide visual feedback (with a loading spinner) when clicked to indicate processing, reducing the likelihood of repeated clicks.

### Testing and Monitoring
Added comprehensive tests for form submissions to simulate various user interactions, ensuring that the issue doesn’t recur.


## Contact Me
**Email:** ouadia@elouardy.com \
**Twitter:** https://twitter.com/_ELOUARDY
