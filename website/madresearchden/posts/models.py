from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from bokeh.embed import server_document

from os import environ


# Create your models here.

class BlogIndexPage(Page):
    """
    """

    max_count = 1

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]

    def get_context(self, request):
        context = super().get_context(request)

        try:
            all_posts = BlogPage.objects.child_of(self).live().public().order_by('-first_published_at')[:9]
            context['blog_posts'] = all_posts
        except:
            pass       

        return context


class BlogPage(Page):
    """
    """
    
    publish_ts = models.DateTimeField(blank=False)
    update_ts = models.DateTimeField(auto_now=True)
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    intro = models.CharField(max_length=250)
    # make this into a struct block? 
    post = StreamField(
        [
            ('section_heading', blocks.CharBlock()), #classname= ??
            ('section_text', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ],
    )

    updates = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('publish_ts'),
        FieldPanel('intro', classname='full'),
        StreamFieldPanel('post')
    ]

    promote_panels = [
        ImageChooserPanel('thumbnail')
    ]

    parent_page_types = ['posts.BlogIndexPage']


class DataVisIndexPage(Page):
    """
    """

    max_count = 1

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]


    def get_context(self, request):
        context = super().get_context(request)

        all_posts = DataVisPage.objects.child_of(self).live().public().order_by('-first_published_at')
        paginator = Paginator(all_posts, 4) # Update to number of posts. 

        page = request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context['data_posts'] = posts

        return context


class DataVisPage(Page):
    """
    """
    
    publish_ts = models.DateTimeField(blank=False)
    update_ts = models.DateTimeField(auto_now=True)
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    intro = models.CharField(max_length=250)
    # make this into a struct block? 
    post = StreamField(
        [
            ('section_heading', blocks.CharBlock()), #classname= ??
            ('section_text', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ],
    )

    bokeh_app = models.CharField(max_length=250, blank=True, null=True)

    updates = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('publish_ts'),
        FieldPanel('intro', classname='full'),
        FieldPanel('bokeh_app'),
        StreamFieldPanel('post')
    ]

    promote_panels = [
        ImageChooserPanel('thumbnail')
    ]

    parent_page_types = ['posts.DataVisIndexPage']

    def get_context(self, request):
        context = super().get_context(request)
       
        script = server_document(f"{environ['BOKEH_URL']}/{self.bokeh_app}")

        context['bokeh_chart'] = script

        return context   


     


