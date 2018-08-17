from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import BlogPost
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.utils import timezone




# Create your views here.


class BlogPostView(DetailView):
    """This class generates views for individual blog posts."""

    model = BlogPost
    template_name = "blog/blogpost.html"

    # was an issue with this not being a func and stopping mysql migrations.
    # get_list_or_404(BlogPost)

    def get_query_set(self):
        return get_list_or_404(BlogPost)


class BlogHomepage(ListView):
    """This is the class the generates the blog homepage view."""

    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = "blog_home_list"

    def get_queryset(self):
        return BlogPost.objects.filter(date_of_post__lte=timezone.now()).order_by("-date_of_post")[:6]


class BlogArchive(ListView):
    """This is the class the generates the blog archive view."""

    model = BlogPost
    template_name = 'blog/archive.html'
    context_object_name = "posts"

    def get_queryset(self):
        """Returns all blogs from a year."""
        blog_list = BlogPost.objects.filter(date_of_post__year=(self.kwargs["year"])).filter(
            date_of_post__lte=timezone.now())
        return get_list_or_404(blog_list)


class BlogArchiveList(ListView):
    """Returns a list of blog entries for a certain year."""

    # TODO a lot of white space. Need to fill this...

    model = BlogPost
    template_name = 'blog/archivelist.html'
    context_object_name = "years"

    def get_queryset(self):
        """Returns a list of unique years from all blog posts."""
        unique = BlogPost.objects.filter(date_of_post__lte=timezone.now())
        unique = unique.dates("date_of_post", "year")
        unique_years = [date.year for date in unique]
        unique_years.sort(reverse=True)
        return unique_years



















