# Github authentication

Start by installing ```social-auth-app-django```

Then include ```social_django``` in ```INSTALLED_APPS```

Next add two ```context_processors```

- social_django.context_processors.backends
- social_django.context_processors.login_redirect


Apply migrations

```bash
python manage.py migrate
```

You will also need to include ```social_django.urls```
in ```users.urls.py```

To use github authentication we have to specify
dedicated authentication backend on top of default authentication backend to ```AUTHENTICATION_BACKENDS``` key

```python
AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.github.GithubOAuth2',
]
```


Add github login to dashboard

```html
<a href="{% url 'social:begin' 'github' %}">Github login</a>
```

You will notice that in above we have used django namespaces. This is Django's way of isolating urls so that they don't clash with each other.

- Unique namespaces avoid application url conflicts
- Social Auth uses namespace **social**
- URLs start with **social:**


## Creating github application

To use github authentication we will have to create a new github application ```https://github.com/settings/applications/new```

Speciffy authorization callback as ```http://localhost:8000/oauth/complete/github```


There is one problem
We have to associate user with the backend before creating it.
Because users can be created with two methods right now.

```python
...
    user = form.save(commit=False)
    user.backend = "django.contrib.auth.backends.ModelBackend"
    user.save()
...
```
