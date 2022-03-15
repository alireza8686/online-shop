from multiprocessing import context
from django.shortcuts import render

from settings.models import SiteInformation

# Create your views here.


def site_information(request):
    setting = SiteInformation.objects.first()
    context = {
        'setting' : setting,
    }
    return render(request,'base/header.html',context)