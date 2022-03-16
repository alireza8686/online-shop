from django.shortcuts import render
from settings.models import SiteInformation
# Create your views here.


def site_information(request):
    setting = SiteInformation.objects.get(id=1)
    context = {
        'setting' : setting,
    }
    return render(request,'home/home.html',context)