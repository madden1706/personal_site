from django.shortcuts import render
#from .models import DataVis
from django.views.generic import DetailView, ListView
from .graphs import test_graph


# Create your views here.
# def testpage(self):
#     return render(self, 'data_vis/data_vis_home.html')

class DataVisHomepage(ListView):
    """This is the class the generates the data vis homepage view."""

    template_name = 'data_vis/data_vis_home.html'

    def get(self, request):
        """Gather data to return to the view."""

        test = test_graph.draw()
        # dict of data for.
        kwargs = {'test1': test, 'test2': 'TEST2'}
        
        return render(request, self.template_name, kwargs)

"""
TODO
Want to have a page that is for returning data vis.
Have the code for making interactive charts with user data in the graphs module. 
"""

# def get_queryset(self):
#     return BlogPost.objects.filter(date_of_post__lte=timezone.now()).order_by("-date_of_post")[:6]