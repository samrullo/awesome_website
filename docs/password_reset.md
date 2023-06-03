# Password reset

To reset password you will have to send reset link to the user email
To test this functionality you can set ```EMAIL_BACKEND``` to ```django.core.mail.backends.console.EmailBackend```

Just as in the case of password change, we will have to create two templates

- users/templates/registration/password_reset_form.html : to display the form for resettings password
- users/templates/registration/password_reset_done.html : to display confirmation that reset link was sent to an email

[Back to main page](../README.md)