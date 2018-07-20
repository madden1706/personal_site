from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import BlogPost
from django.views.generic import DetailView, ListView


# Create your views here.


class BlogPostView(DetailView):
    """This class generates views for individual blog posts."""

    model = BlogPost
    template_name = "blog/blogpost.html"
    get_list_or_404(BlogPost)
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
        """Returns all blogs from a year."""
        return get_list_or_404(BlogPost.objects.filter(
            date_of_post__year=self.kwargs["year"]))


class BlogArchiveList(ListView):
    """Returns a list of blog entries for a certain year."""

    # TODO a lot of white space. Need to fill this...

    model = BlogPost
    template_name = 'blog/archivelist.html'
    context_object_name = "years"

    def get_queryset(self):
        """Returns a list of unique years from all blog posts."""
        unique = BlogPost.objects.dates("date_of_post", "year")
        unique_years = [date.year for date in unique]
        unique_years.sort(reverse=True)
        return unique_years




















