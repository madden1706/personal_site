from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class DataVis(models.Model):
    """A class for data vis posts."""

    title_of_post = models.CharField(max_length=200)
    date_of_post = models.DateField()
    slug = models.SlugField(default="", blank=True) # remove from admin page view. Or, not editable. 
    seo_description = models.CharField(max_length=200)
    publish = models.BooleanField()
    intro_text = models.TextField(default='')

    template_to_use = models.CharField(choices=[['altair', 'Altair'], ['bokeh', 'Bokeh']], default='', max_length=10)
    # this should be an image upload..... 
    homepage_chart_image = models.ImageField(upload_to = "static/images/data_vis" )

    def __str__(self):
        return self.title_of_post

    def _get_pk_val(self, meta=None):
        return self.pk

    def slug_value(self):
        return self.slug

    def save(self, *args, **kwargs):
        '''This remakes the url on EACH save with a prettier slugified_url_like_this - be careful of overwriting.'''
        self.slug = slugify(self.title_of_post)
        super(DataVis, self).save(*args, **kwargs)

    # Note: this enables the "View on Site" button in the admin page.     
    def get_absolute_url(self):    
        return reverse('data_vis:data_vis_post', kwargs={'slug': self.slug, 'pk': self.pk})


class DataVisFigure(models.Model):
    """A class for figures with a many to relationship with DataVis."""
    
    data_vis = models.ForeignKey(DataVis, on_delete=models.CASCADE)
    graph_title = models.CharField(max_length=200)
    json_graph = models.TextField()
 #   main_fig = models.BooleanField(default=False) # This is used for the thumbnail and if the post is featured to specify the main figure.
 #   view_order = models.IntegerField(default=0)
    fig_text = models.TextField(default='')



