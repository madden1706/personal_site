from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import date

# Create your models here.

class DataVis(models.Model):
    """A class for data vis posts."""

    title_of_post = models.CharField(max_length=200)
    date_of_post = models.DateField(default=date.today)
    slug = models.SlugField(default="", blank=True) # remove from admin page view. Or, not editable. 
    seo_description = models.CharField(max_length=200)
    publish = models.BooleanField(default=False)
    intro_text = models.TextField(default='')

    template_to_use = models.CharField(choices=[['altair', 'Altair'], ['bokeh', 'Bokeh']], default='', max_length=10)
    # this should be an image upload..... 
    # How should this be named?
    homepage_chart_image = models.ImageField(upload_to="images/data_vis", blank=True, default='')

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
    json_graph = models.TextField(default='')
 #   main_fig = models.BooleanField(default=False) # This is used for the thumbnail and if the post is featured to specify the main figure.
 #   view_order = models.IntegerField(default=0)
    fig_text = models.TextField(default='')


class DataVisInteractive(models.Model):
    """A class for interactive bokeh server data vis posts."""

    title_of_post = models.CharField(max_length=200)
    date_of_post = models.DateField(default=date.today)
    slug = models.SlugField(default="", blank=True) # remove from admin page view. Or, not editable. 
    seo_description = models.CharField(max_length=200)
    publish = models.BooleanField(default=False)
    intro_text = models.TextField(default='')  
    bokeh_app_name = models.CharField(max_length=200)
    concluding_text = models.TextField(default='')
    # this should be an image upload..... 
    homepage_chart_image = models.ImageField(upload_to = "bokeh_apps/data_vis_interactive", blank=True, default='')

    def __str__(self):
        return self.title_of_post

    def _get_pk_val(self, meta=None):
        return self.pk

    def slug_value(self):
        return self.slug

    def save(self, *args, **kwargs):
        '''This remakes the url on EACH save with a prettier slugified_url_like_this - be careful of overwriting.'''
        self.slug = slugify(self.title_of_post)
        super(DataVisInteractive, self).save(*args, **kwargs)

    # Note: this enables the "View on Site" button in the admin page.     
    def get_absolute_url(self):    
        return reverse('data_vis:interactive_data_vis_page', kwargs={'slug': self.slug, 'pk': self.pk})


