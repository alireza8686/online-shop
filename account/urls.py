from django.urls import path

from .views import login_view , register_view , log_out , user_panel

urlpatterns = [
    path("login/", login_view,name='login'),
    path("register/", register_view,name='register'),
    path("panel/", user_panel,name="panel"),
#     path("panel/edit", panel_edit),
    path("log-out/", log_out,name='logout')
]