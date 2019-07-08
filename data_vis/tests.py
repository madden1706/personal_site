from django.test import TestCase
from .models import DataVis, DataVisFigure
from django.utils import timezone

# Create your tests here.

def create_datavis(days, publishable):
    """For checks that the only future data vis posts are display. """
    time = timezone.now() + datetime.timedelta(days=days)
    DataVisFigure.objects.create(title_of_post="Test Post"
    , date_of_post=days,
    publish=publishable)


class DataVisTest(TestCase):

    def test_if_not_publishable_filtered():

        test_case = create_datavis(0, True):
        
        pass

    def test_if_future_filtered():
        pass

class DataVisFigureTest(TestCase):
    pass
