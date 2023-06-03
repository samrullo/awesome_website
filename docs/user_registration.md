# User registration
Django doesn't come equipped with user creation forms.
However we can create our own forms

```UserCreationForm``` contains necessary fields to create a user but it doesn't include ```email``` field

- username
- password1
- password2

No worries, we can define our own custom user creation form by subclassing UserCreationForm

```python
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
```

