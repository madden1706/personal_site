from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import DataVis, DataVisFigure
from django.views.generic import DetailView, ListView
from django.utils import timezone
from django.http import Http404
from .graphs import test_graph


# Create your views here.
# def testpage(self):
#     return render(self, 'data_vis/data_vis_home.html')

class DataVisHomepage(ListView):
    """This is the class the generates the data vis homepage view."""

    template_name = 'data_vis/data_vis_home.html'
    context_object_name = "data_vis_list"

    def get_queryset(self):
        """Returns all blogs from a year."""
        # date_of_post__lte=timezone.now().filter(publish=True
        data_vis_list = DataVis.objects.filter(publish=True).filter(date_of_post__lte=timezone.now())[:2]
        # print(data_vis_list.values()[0]['id']) # this is a list of dicts.
        return data_vis_list

    # def get(self, request):
    #     """Gather data to return to the view."""
    #     test = test_graph.draw()
    #     # dict of data for.
    #     kwargs = {'test1': test, 
    #         'test2': 'TEST2',
    #         'data_vis_list': ''}        
        
    #     return render(request, self.template_name, kwargs)

"""
TODO
Want to have a page that is for returning data vis.
Have the code for making interactive charts with user data in the graphs module. 
"""

def data_vis_post(request, slug, pk):

    data = get_object_or_404(DataVis, pk=pk, slug=slug)
    if data.publish == True:
        return render(request, 'data_vis/data_vis_page.html', {'datavis': data})
    else:
        raise Http404() 




