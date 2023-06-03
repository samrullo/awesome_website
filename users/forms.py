from django.contrib.auth.forms import UserCreationForm

# because we want to change fields attribute of super class we resort to Meta
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)