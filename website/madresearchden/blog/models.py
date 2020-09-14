from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

# Create your models here.

class BlogIndexPage(Page):
    """
    """

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]


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

    parent_page_types = ['blog.BlogIndexPage']


     


