from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone
# Create your models here.


class BlogPost(models.Model):
    """A class for making blog posts."""

    title_of_post = models.CharField(max_length=200)
    date_of_post = models.DateField()
    blog_post = models.TextField()
    slug = models.SlugField(default="", blank=True)
    seo_description = models.CharField(max_length=200)
    publish = models.BooleanField(default=True)

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
        '''This remakes the url on EACH save with a prettier slugified_url_like_this - be careful of overwriting.'''
        self.slug = slugify(self.title_of_post)
        super(BlogPost, self).save(*args, **kwargs)

    def get_next(self):
        """This function will return the next post by date, unless it is in the future (in which case it returns nothing
        Used for the next button on the blog post page."""
        try:
            return BlogPost.objects.filter(date_of_post__lte=timezone.now()).filter(date_of_post__gt=self.date_of_post).order_by("-date_of_post")[0]
        except:
            None


class SeoKeyword(models.Model):
    """A class for holding SEO keywords for blog posts, many-to-one with BlogPost.seo_keywords"""

    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=50)





    # def previous(self):
    # p = BlogPost.objects.filter(date_of_post__lte=self.date_of_post)[:1].values('pk')

    # BlogPost.objects.objects.dates("date_of_post", "year", order='DESC') #gets the unique values for year






















