from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.blocks import StructBlock, PageChooserBlock

from posts.models import BlogPage, DataVisPage


class HomePage(Page):

    max_count = 1

    body = RichTextField(blank=True)
    #promote_pages = HomePagePromote()
    

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        #FieldPanel('promote_pages', classname="full"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        
        try:
            context['blog_post'] = BlogPage.objects.live().public().order_by('-first_published_at')[0]# #child_of(self).live()
        except:
            pass

        try:
            context['data_post'] = DataVisPage.objects.live().public().order_by('-first_published_at')[0]# #child_of(self).live()
        except:
            pass


        return context


class AboutMe(Page):

    max_count = 1

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        #FieldPanel('promote_pages', classname="full"),
    ]



