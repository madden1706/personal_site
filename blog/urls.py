from django.urls import path, re_path
from . import views
from blog.views import BlogPostView, BlogHomepage, BlogArchive, BlogArchiveList
from .models import BlogPost


app_name = "blog"

urlpatterns = [
    path('', views.BlogHomepage.as_view(), name='blog'),
    path('<slug:slug>_<pk>/', views.BlogPostView.as_view(), name="blog_post"),
    path('archive/<int:year>/', views.BlogArchive.as_view(), name="blog_archive"),
    path('archive/list/', views.BlogArchiveList.as_view(), name="blog_archive_list"),
]




