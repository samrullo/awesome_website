from django.contrib.auth import login
from django.shortcuts import render,redirect
from django.urls import reverse
from users.forms import CustomUserCreationForm


# About reverse function
# The purpose of the reverse function in the given code is to dynamically generate the URL for the "dashboard" view and redirect the user to that URL after successful registration.
# In Django, URLs are typically defined using named URL patterns in the URL configuration. The reverse function allows you to obtain the URL associated with a given view name by reversing the URL patterns defined in your project.
# By using reverse("dashboard"), the code retrieves the URL associated with the view named "dashboard" and passes it to the redirect function. This ensures that the user is redirected to the correct URL for the dashboard page, regardless of any changes to the URL configuration.
# Overall, the reverse function helps maintain flexibility and decoupling between the view code and the specific URL paths, making it easier to update and manage the URL structure of your application.


# Create your views here.
def dashboard(request):
    return render(request,'users/dashboard.html',)

def register(request):
    if request.method == 'GET':
        return render(request,'users/register.html',{"form":CustomUserCreationForm})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend="django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request,user)
            return redirect(reverse("dashboard"))