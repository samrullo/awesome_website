# Handle password reset email

As seen earlier, we can send reset link to user email.

Then to handle actual reset, we have to create two templates

- users/templates/registration/password_reset_confirm.html : somewhat confusingly this will display the form to reset password
- users/templates/registration/password_reset_complete.html : again confusingly this is confirmation that reset is complete. easy to confuse it with password_reset_done.html which is confirmatino page for sending reset link

You can override reset email body and subject using below files

- users/templates/registration/password_reset_email.html
- users/templates/registratiion/password_reset_subject.txt

[Back to main page](../README.md)