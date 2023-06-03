# Login

We need to create ```registration/login.html``` under templates for ```login``` view to show login form

```html
<form method="post">

{% csrf_token %}

{{form.as_p}}
<input type="submit" value="Login">

</form>
```

when using forms, django requires to have ```csrf_token``` to prevent cross site forgery attacks.
```form``` variable is already included in the context, provided by ```django.contrib.auth``` most probably.

Once we login, django redirects us to ```accounts/profile``` route.
We can set ```LOGIN_REDIRECT_URL``` setting to ```dashboard``` in our project settings.py file

[Back to main page](../README.md)