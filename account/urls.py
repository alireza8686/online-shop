from django.urls import path

from .views import login_view, panel_edit , register_view , log_out , user_panel

urlpatterns = [
    path("login/", login_view,name='login'),
    path("register/", register_view,name='register'),
    path("panel/", user_panel,name="panel"),
    path("panel/edit/", panel_edit,name='panel-edit'),
    path("log-out/", log_out,name='logout')
]