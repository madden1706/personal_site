from django.test import TestCase
from .models import DataVis, DataVisFigure
from django.utils import timezone
from django.urls import reverse
import datetime

# Create your tests here.

def create_datavis(title, days, publishable, homepage_img, template):
    """ Creates a test DataVis post x days in the future and bool publishable. """
    time = timezone.now() + datetime.timedelta(days=days)

    return  DataVis.objects.create(title_of_post=title, 
    date_of_post=time, 
    publish=publishable,
    homepage_chart_image=homepage_img,
    intro_text = 'Intro text', 
    seo_description = 'SEO',
    template_to_use=template)


# Functions for making published/not posts. 
def true_publish_post_bokeh(): 
    return create_datavis(title='Test_True', days=-1, publishable=True, template='bokeh',
    homepage_img='static/images/data_vis/visualization1.png')

def false_publish_post_bokeh(): 
    return create_datavis(title='Test_False', days=-1, publishable=False, template='bokeh',
    homepage_img='static/images/data_vis/visualization1.png')

def true_publish_post_altair(): 
    return create_datavis(title='Test_True', days=-1, publishable=True, template='altair',
    homepage_img='static/images/data_vis/visualization1.png')

def false_publish_post_altair(): 
    return create_datavis(title='Test_False', days=-1, publishable=False, template='altair',
    homepage_img='static/images/data_vis/visualization1.png')


class DataVisTest(TestCase):

    def test_publishable_post_altair(self):
        test_post = true_publish_post_altair()
        url = reverse('data_vis:data_vis_post', kwargs={'pk': test_post.id, 'slug': test_post.slug })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_post.title_of_post)   

    def test_not_publishable_post_altair(self):
        test_post = false_publish_post_altair()
        url = reverse('data_vis:data_vis_post', kwargs={'pk': test_post.id, 'slug': test_post.slug })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_publishable_post_bokeh(self):
        test_post = true_publish_post_bokeh()
        url = reverse('data_vis:data_vis_post', kwargs={'pk': test_post.id, 'slug': test_post.slug })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_post.title_of_post)   

    def test_not_publishable_post_bokeh(self):
        test_post = false_publish_post_bokeh()
        url = reverse('data_vis:data_vis_post', kwargs={'pk': test_post.id, 'slug': test_post.slug })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class DataVisHomeView(TestCase):

    def test_no_posts(self):
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no data right now...")
        self.assertQuerysetEqual(response.context['data_vis_list'], [])

    def test_publishable_posts_altair(self):
        test_post = true_publish_post_altair()
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['data_vis_list'], ['<DataVis: Test_True>'])
        self.assertContains(response, test_post.title_of_post)

    def test_no_publishable_posts_altair(self):
        test_post = false_publish_post_altair()
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no data right now...")
        self.assertQuerysetEqual(response.context['data_vis_list'], [])
        self.assertNotContains(response, test_post.title_of_post)

    def test_publishable_posts_bokeh(self):
        test_post = true_publish_post_bokeh()
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['data_vis_list'], ['<DataVis: Test_True>'])
        self.assertContains(response, test_post.title_of_post)

    def test_no_publishable_posts_bokeh(self):
        test_post = false_publish_post_bokeh()
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no data right now...")
        self.assertQuerysetEqual(response.context['data_vis_list'], [])
        self.assertNotContains(response, test_post.title_of_post)

    def test_publishable_and_no_publishable_posts(self):
        """Only did the one combo of altair templates for this test."""
        test_post = true_publish_post_altair()
        test_post_false = false_publish_post_altair()
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['data_vis_list'], ['<DataVis: Test_True>'])
        self.assertContains(response, test_post.title_of_post)
        self.assertNotContains(response, test_post_false.title_of_post)


