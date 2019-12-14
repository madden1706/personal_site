
import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from data_vis.models import DataVis,DataVisInteractive

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

    time = timezone.now() - datetime.timedelta(days=date)

    return DataVis.objects.create(title_of_post=title, 
        date_of_post=time, 
        intro_text=post, 
        publish=publishable)


class HomepageDataVis(TestCase):

    # python manage.py test homepage

    def test_main_datavis_int_post(self):        
        """        
        :return:
        """
        test = create_data_vis_int("Data Vis Int Title", -10, "Post text", True)
        response = self.client.get(reverse('homepage:homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test.title_of_post)
        #self.assertQuerysetEqual(response.context['data_vis_int_main'], f'<DataVisInteractive: {test.title_of_post}>')


    # def test_main_datavis_post(self):
    #     """
        
    #     :return:
    #     """

    #     create_data_vis("Data Vis Title", 10, "Post text", True)
    #     response = self.client.get(reverse('homepage:homepage'))
    #     self.assertContains(response, "Data Vis Title")
    #     #self.assertQuerysetEqual(response.context['data_vis_main'], [])
