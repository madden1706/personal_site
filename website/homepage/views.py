from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from django.utils import timezone

from blog.models import BlogPost
from data_vis.models import DataVis, DataVisInteractive

import datetime

# Create your views here.



def homepage(self):

    """
    If there is an interactive post return that.
    If not return a data vis post.

    Return most recent 3 blog posts.
    """

    data_vis_main = []
    data_vis_int_main = []
    blogpost = []
    secondary_posts = []
    secondary_data_vis = []

    try:
        data_vis_main = DataVis.objects.filter(
            date_of_post__lte=timezone.now()
            ).filter(
            publish=True
            ).order_by("-date_of_post")[0]
    except:
        data_vis_main = []

    try:
        data_vis_int_main = DataVisInteractive.objects.filter(
            date_of_post__lte=timezone.now()
            ).filter(
            publish=True
            ).order_by("-date_of_post")[0]
    except:
        data_vis_int_main = []

    if data_vis_main and data_vis_int_main:
        
        # Feature an interactive post over a normal most recent data vis post. 30 day limit. 
        if (data_vis_main.date_of_post - datetime.timedelta(days=30)) > data_vis_int_main.date_of_post:
            data_vis_int_main = []
        elif (data_vis_main.date_of_post - datetime.timedelta(days=30)) < data_vis_int_main.date_of_post:
            data_vis_main = []
        else:
            data_vis_main = []

    elif data_vis_main and not data_vis_int_main:
        data_vis_int_main = []
    
    elif not data_vis_main and data_vis_int_main:
        data_vis_main = []       

    else:
        data_vis_main = []
        data_vis_int_main = []

    # Try to get the most recent blogpost
    try:
        blogpost = BlogPost.objects.filter(
            date_of_post__lte=timezone.now()
            ).filter(
            publish=True
            ).order_by("-date_of_post")[0]
    except:
        blogpost = []

    # If there is a main blogpost - get older posts as secondary posts to feature. 
    if blogpost:
        secondary_blogposts = BlogPost.objects.filter(
            date_of_post__lte=timezone.now()
            ).filter(
            publish=True
            ).order_by("-date_of_post")[1:3]
    else:
        secondary_blogposts = []    


    data = {'data_vis_main': data_vis_main,
        'data_vis_int_main': data_vis_int_main, 
        'blogpost': blogpost, 
        'secondary_blogposts': secondary_blogposts,
        'secondary_datavis': secondary_data_vis}

    template = 'homepage/homepage.html'

    return render(self, template, data)


# def homepage(self): 
#     return render(self, 'homepage/homepage.html')


def testpage(self):
    return render(self, 'homepage/testpage.html')


def about_me(self):
    return render(self, 'homepage/aboutme.html')


def contact(self):
    return render(self, 'homepage/contact.html')


def custom_404(self, exception):
    return render(self, "homepage/404.html")


def custom_500(self):
    return render(self, "homepage/500.html")
