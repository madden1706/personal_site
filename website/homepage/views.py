from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView

from blog.models import BlogPost
from data_vis.models import DataVis

from django.utils import timezone

# Create your views here.


def homepage(self):

    # Get most recent data vis post
    # get last blog post
    blogpost = BlogPost.objects.filter(
        date_of_post__lte=timezone.now()
        ).filter(publish=True
        ).order_by("-date_of_post")[0]

    data_vis = DataVis.objects.filter(
        date_of_post__lte=timezone.now()
        ).filter(
        publish=True
        ).order_by("date_of_post")[1]

    print("------------", data_vis)
    data = {'datavis': data_vis, 'blogpost': blogpost}
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
