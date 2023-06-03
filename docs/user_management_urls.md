# User management urls

By including ```django.contrib.auth.urls``` in our ```users.urls``` we get access to 

- accounts/login 
- accounts/logout
- accounts/password_change : Used to change a password
- accounts/password_change/done : shows a confirmation that password was changed
- accounts/password_reset : Used to request an email with password reset link
- accounts/password_reset/done : Shows a confirmation that a password reset mail was sent
- accounts/reset/<uidb64>/<token>/ : Used to set a new password using password reset link
- accounts/reset/done : Show confirmation that reset was done

[Back to main page](../README.md)