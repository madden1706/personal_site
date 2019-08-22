from django.urls import path, re_path
from . import views

from .models import BlogPost


app_name = "blog"

urlpatterns = [
    path('', views.BlogHomepage.as_view(), name='blog'),
    path('<slug:slug>_<pk>/', views.blogpost, name="blog_post"),
    path('archive/<int:year>/', views.BlogArchive.as_view(), name="blog_archive"),
    path('archive/list/', views.BlogArchiveList.as_view(), name="blog_archive_list"),
]




