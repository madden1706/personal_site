from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.


class BlogPost(models.Model):
    """A class for making blog posts."""

    title_of_post = models.CharField(max_length=200)
    date_of_post = models.DateField()
    blog_post = models.TextField()
    slug = models.SlugField(default="", blank=True)

    def get_absolute_url(self):
        """This is for the previous/next buttons."""
        return reverse("blog:blog_post", kwargs={"pk": BlogPost._get_pk_val(self), "slug": BlogPost.slug_value(self)})

    def __str__(self):
        return self.title_of_post

    def _get_pk_val(self, meta=None):
        return self.pk

    def slug_value(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_of_post)
        super(BlogPost, self).save(*args, **kwargs)





    # def previous(self):
    # p = BlogPost.objects.filter(date_of_post__lte=self.date_of_post)[:1].values('pk')

    # BlogPost.objects.objects.dates("date_of_post", "year", order='DESC') #gets the unique values for year






















