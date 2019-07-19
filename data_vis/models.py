from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class DataVis(models.Model):
    """A class for data vis posts."""

    title_of_post = models.CharField(max_length=200)
    date_of_post = models.DateField()
    slug = models.SlugField(default="", blank=True) # remove from admin page view. Or, not editable. 
    seo_description = models.CharField(max_length=200)
    publish = models.BooleanField()
    intro_text = models.TextField(default='')
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


#TODO have a foreign key relationship to graphs.
# have these in html figures. 
# add a publish column? Filter queries for only those to publish. -- need to change the crawling of site to reflect this. 
# How to have a featured post -  not by date, but nominated. 

# Variable width content via Bootstrap fields (for white v bars on pages. )


class DataVisFigure(models.Model):
    """A class for figures with a many to relationship with DataVis."""
    
    data_vis = models.ForeignKey(DataVis, on_delete=models.CASCADE)
    graph_title = models.CharField(max_length=200)
    json_graph = models.TextField()
    main_fig = models.BooleanField() # This is used for the thumbnail and if the post is featured to specify the main figure.
    view_order = models.IntegerField(default=0)
    fig_text = models.TextField(default='')

