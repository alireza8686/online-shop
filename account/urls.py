from django.urls import path

from .views import login_view

urlpatterns = [
    path("login", login_view,name='login'),
#     path("register", register_page),
#     path("panel", user_panel),
#     path("panel/edit", panel_edit),
#     path("log-out", log_out)
]