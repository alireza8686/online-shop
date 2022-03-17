from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import *

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        redirect("home")

    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            context = {
                'error' : 'نام کاربری یا رکز عبور اشتباه میباشد',
            }
            return render(request, "account/login.html", context)
    context = {
        "login_form": login_form
    }
    return render(request, "account/login.html", context)