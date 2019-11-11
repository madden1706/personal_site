
import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from data_vis.models import DataVis, DataVisInteractive

# Create your tests here.


def create_data_vis_int(title, date, post, publishable):
    """
    :param title: Title of a blog post.
    :param date: Date of the blog post.
    :param post: Content of a blog post.
    :return: An interactive data vis post with a specified date, +int for future (days) and -int for past.
    """

    time = timezone.now() + datetime.timedelta(days=date)

    return DataVisInteractive.objects.create(title_of_post=title, 
        date_of_post=time, 
        intro_text=post, 
        publish=publishable)


def create_data_vis(title, date, post, publishable):
    """
    :param title: Title of a blog post.
    :param date: Date of the blog post.
    :param post: Content of a blog post.
    :return: A data vis post with a specified date, +int for future (days) and -int for past.
    """

    time = timezone.now() + datetime.timedelta(days=date)

    return DataVis.objects.create(title_of_post=title, 
        date_of_post=time, 
        intro_text=post, 
        publish=publishable)


class HomepageDataVis(TestCase):

    # python manage.py test homepage

    def test_main_datavis_int_post(self):        
        test = create_data_vis_int("Data Vis Int Title", -10, "Post text", True)
        response = self.client.get(reverse('homepage:homepage'))
        test_model = test.__class__.__name__
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test.title_of_post)
        # The query set is 1 piece of data, so needs to be put iterable here i.e. I stuck it in a list.
        self.assertQuerysetEqual([response.context['data_vis_int_main']], [f"<{test_model}: {test}>"])

    def test_main_datavis_post(self):
        test = create_data_vis("Data Vis Title", -10, "Post text", True)
        response = self.client.get(reverse('homepage:homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test.title_of_post)

    def test_main_datavis_int_post_future(self):        
        test = create_data_vis_int("Data Vis Int Title", 10, "Post text", True)
        response = self.client.get(reverse('homepage:homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are currently no data visualisation posts.")

    def test_main_datavis_post_future(self):
        test = create_data_vis("Data Vis Title", 10, "Post text", True)
        response = self.client.get(reverse('homepage:homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are currently no data visualisation posts.")

    def test_main_datavis_int_post_newest(self):        
        test = create_data_vis_int("Data Vis Int Title", -10, "Post text", True)
        data_vis_test = create_data_vis("Data Vis Title", -10, "Post DataVis text", True)
        response = self.client.get(reverse('homepage:homepage'))
        self.assertEqual(response.status_code, 200)
        test_model = test.__class__.__name__
        # print(response.context['data_vis_int_main'], f"<{test_model}: {test}>")
        self.assertQuerysetEqual([response.context['data_vis_int_main']], [f"<{test_model}: {test}>"])
        self.assertQuerysetEqual([response.context['data_vis_main']], ["[]"])
        self.assertQuerysetEqual([response.context['blogpost']], ["[]"])
        self.assertQuerysetEqual([response.context['secondary_blogposts']], ["[]"])
        self.assertQuerysetEqual([response.context['secondary_datavis']], ["[]"])
        self.assertContains(response, test.title_of_post)

    def test_main_datavis_post_newest(self):        
        test = create_data_vis_int("Data Vis Int Title", -45, "Post text", True)
        data_vis_test = create_data_vis("Data Vis Title", -10, "Post DataVis text", True)
        response = self.client.get(reverse('homepage:homepage'))
        self.assertEqual(response.status_code, 200)
        data_vis_test_model = data_vis_test.__class__.__name__
        self.assertQuerysetEqual([response.context['data_vis_int_main']], ["[]"])
        self.assertQuerysetEqual([response.context['data_vis_main']], [f"<{data_vis_test_model}: {data_vis_test}>"])
        self.assertQuerysetEqual([response.context['blogpost']], ["[]"])
        self.assertQuerysetEqual([response.context['secondary_blogposts']], ["[]"])
        self.assertQuerysetEqual([response.context['secondary_datavis']], ["[]"])
        self.assertContains(response, data_vis_test.title_of_post)

    def test_main_datavis_int_post_equals_datavis_post_age(self):        
        test = create_data_vis_int("Data Vis Int Title", -40, "Post text", True)
        data_vis_test = create_data_vis("Data Vis Title", -10, "Post DataVis text", True)
        response = self.client.get(reverse('homepage:homepage'))
        self.assertEqual(response.status_code, 200)
        test_model = test.__class__.__name__
        # print(response.context['data_vis_int_main'], f"<{test_model}: {test}>")
        self.assertQuerysetEqual([response.context['data_vis_int_main']], [f"<{test_model}: {test}>"])
        self.assertQuerysetEqual([response.context['data_vis_main']], ["[]"])
        self.assertQuerysetEqual([response.context['blogpost']], ["[]"])
        self.assertQuerysetEqual([response.context['secondary_blogposts']], ["[]"])
        self.assertQuerysetEqual([response.context['secondary_datavis']], ["[]"])
        self.assertContains(response, test.title_of_post)

