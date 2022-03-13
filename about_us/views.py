from django.shortcuts import render
from .models import *
# Create your views here.


def about_us(request):
    abouts_us = AboutUs.objects.all()
    our_team = OurTeam.objects.all()
    context = {
        "about_us": abouts_us,
        "our_team": our_team
    }
    return render(request, "about_us/about-us.html", context)