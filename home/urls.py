from django.urls import path
from .views import site_information


urlpatterns = [
    path('',site_information,name='site-information')
]
