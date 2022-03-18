from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import *

# Create your views here.


def login_view(request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            login_form = LoginForm()
            context = {
                'error' : 'نام کاربری یا رمز عبور اشتباه میباشد',
                "login_form": login_form,
            }
            return render(request, "account/login-page.html", context)
    context = {
        "login_form": login_form
    }
    return render(request, "account/login-page.html", context)



def register_view(request):

    register_form = RegisterForm(request.POST)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect("/login")

    context = {
        "register_form": register_form
    }
    return render(request, "account/register-page.html", context)


