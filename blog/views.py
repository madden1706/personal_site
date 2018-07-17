from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.views.generic import DetailView, ListView


# Create your views here.


class BlogPostView(DetailView):
    """This class generates views for individual blog posts."""

    model = BlogPost
    template_name = "blog/blogpost.html"
    # TODO Class view returns a 404 if there is on pk automatically? what if blog/gg ???


class BlogHomepage(ListView):
    """This is the class the generates the blog homepage view."""

    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = "blog_home_list"

    def get_queryset(self):
        return BlogPost.objects.all().order_by("-date_of_post")[:3]


class BlogArchive(ListView):
    """This is the class the generates the blog archive view."""

    model = BlogPost
    template_name = 'blog/archive.html'
    context_object_name = "posts"

    def get_queryset(self):
        return BlogPost.objects.filter(date_of_post__year=self.kwargs["year"])


class BlogArchiveList(ListView):

    # TODO a lot of white space. Need to fill this...

    model = BlogPost
    template_name = 'blog/archivelist.html'
    context_object_name = "years"

    def get_queryset(self):
        unique = BlogPost.objects.dates("date_of_post", "year")
        unique_years = [date.year for date in unique]
        unique_years.sort(reverse=True)
        return unique_years




















