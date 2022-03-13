from django.urls import path

from .views import BlogList, blog_detail

urlpatterns = [
    path("blogs/", BlogList.as_view(),name='blog-list'),
    # path("blog/search", SearchBlog.as_view()),
    path("blog/<int:pk>/", blog_detail,name='blog-detail'),
]