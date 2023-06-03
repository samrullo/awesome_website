# User management

# Creating project and app
First as usual we create a project and an application called users.
We will add our users application to installed apps

```bash
django-admin startproject config .
```

```bash
python manage.py startapp users
```

# Creating views
Unders ```users``` we create ```templates``` folder. Under it we create ```users/``` and ```registration/``` folders.
Under ```templates``` folder we create ```base.html``` which will serve as our base template.
```users/dashboard.html``` will serve as our dashboard view and extends base.html

In users.views we define view for dashboard.

```python
from django.shortcuts import render

def dashboard(request):
    return render('users/dashboard.html')
```

# Next contents
- [User management urls](docs/user_management_urls.md)
- [Login](docs/login.md)
- [Password Change](docs/password_change.md)
- [Password reset](docs/password_reset.md)
- [Handle password reset email](docs/handle_password_reset_email.md)