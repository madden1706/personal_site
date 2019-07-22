from django.test import TestCase
from .models import DataVis, DataVisFigure
from django.utils import timezone
from django.urls import reverse
import datetime

# Create your tests here.

def create_datavis(title, days, publishable, homepage_img):
    """ Creates a test DataVis post x days in the future and bool publishable. """
    time = timezone.now() + datetime.timedelta(days=days)

    return  DataVis.objects.create(title_of_post=title, 
    date_of_post=time, 
    publish=publishable,
    homepage_chart_image=homepage_img,
    intro_text = 'Intro text', 
    seo_description = 'SEO' )


# Functions for making published/not posts. 
def true_publish_post(): 
    return create_datavis(title='Test_True', days=-1, publishable=True, 
    homepage_img='static/images/data_vis/visualization1.png')

def false_publish_post(): 
    return create_datavis(title='Test_True', days=-1, publishable=False, 
    homepage_img='static/images/data_vis/visualization1.png')


class DataVisTest(TestCase):

    def test_publishable_post(self):
        test_post = true_publish_post()
        url = reverse('data_vis:data_vis_post', kwargs={'pk': test_post.id, 'slug': test_post.slug })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_post.title_of_post)   

    def test_not_publishable_post(self):
        test_post = false_publish_post()
        url = reverse('data_vis:data_vis_post', kwargs={'pk': test_post.id, 'slug': test_post.slug })
        print(url)
        response = self.client.get(url)
        print("ROSS ######", response)
        self.assertEqual(response.status_code, 404)
        

class DataVisHomeView(TestCase):

    def test_no_posts(self):
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no data right now...")
        self.assertQuerysetEqual(response.context['data_vis_list'], [])

    def test_publishable_posts(self):
        test_post = true_publish_post()
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['data_vis_list'], ['<DataVis: Test_True>'])
        self.assertContains(response, test_post.title_of_post)

    def test_no_publishable_posts(self):
        test_post = false_publish_post()
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no data right now...")
        self.assertQuerysetEqual(response.context['data_vis_list'], [])

    def test_publishable_and_no_publishable_posts(self):
        test_post = true_publish_post()
        test_post_false = false_publish_post()
        response = self.client.get(reverse('data_vis:data_vis'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['data_vis_list'], ['<DataVis: Test_True>'])
        self.assertContains(response, test_post.title_of_post)


