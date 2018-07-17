from django.db import models
from django.urls import reverse
# Create your models here.


class BlogPost(models.Model):
    """A class for making blog posts."""

    title_of_post = models.CharField(max_length=200)
    date_of_post = models.DateField()
    blog_post = models.TextField()

    def get_absolute_url(self):
        return reverse("blog:blog_post", kwargs={"pk": BlogPost._get_pk_val(self)})

    def preview(self):
        return str(self.blog_post)[0:200]

    def __str__(self):
        return self.title_of_post

    def _get_pk_val(self, meta=None):
        return self.pk

    # def previous(self):
    # p = BlogPost.objects.filter(date_of_post__lte=self.date_of_post)[:1].values('pk')

    # BlogPost.objects.objects.dates("date_of_post", "year", order='DESC') #gets the unique values for year






















