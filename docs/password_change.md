# Password change

Will need to define two templates.
One for displaying the form to change password
Another to display a page to tell the user that password was changed successfully

- users/templates/registration/password_change_form.html
- users/templates/registration/password_change_done.html

password change form page will look almost same as login form

```html
{% block content %}

<form method="post">
{% csrf_token %}

{{form.as_p}}

<input type="submit" value="Submit">
</form>

{% endblock %}
```

Finally, you can provide link to password change as href attribute ```{%url 'password_change'%}```

[Back to main page](../README.md)