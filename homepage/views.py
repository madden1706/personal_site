from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(self):
    return render(self, 'homepage/homepage.html')


def testpage(self):
    return render(self, 'homepage/testpage.html')


def about_me(self):
    return render(self, 'homepage/aboutme.html')


def contact(self):
    return render(self, 'homepage/contact.html')

def my_custom_page_not_found(self):
    return render(self, 'homepage/404.html')
