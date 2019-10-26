from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import DataVis, DataVisFigure, DataVisInteractive
from django.views.generic import DetailView, ListView
from django.utils import timezone
from django.http import Http404
from os import system, environ
from .graphs import test_graph

from bokeh.embed import server_document, components

# Create your views here.

class DataVisHomepage(ListView):
    """This is the class the generates the data vis homepage view."""

    template_name = 'data_vis/data_vis_home.html'

    def get_queryset(self):
        """ """

        # This logic is tho get the most recent data_vis/int post (with a preference for an interactive post) for the data vis homepage.
        try:
            data_vis = DataVis.objects.filter(publish=True).filter(date_of_post__lte=timezone.now()).order_by("-date_of_post")[0]
        except:
            data_vis = ""

        try:
            data_vis_int = DataVisInteractive.objects.filter(publish=True).filter(date_of_post__lte=timezone.now()).order_by("-date_of_post")[0]
        except:
            data_vis_int = ""

        # Get other posts. Main post is filtered out in the get() below.
        # other_int = DataVis.objects.filter(publish=True).filter(date_of_post__lte=timezone.now())[1:5]
        # other_data_vis = DataVisInteractive.objects.filter(publish=True).filter(date_of_post__lte=timezone.now())[1:5] 

        # other_data = other_int.values_list('title_of_post', 'date_of_post', 'intro_text', 'homepage_chart_image').union(
        #     other_data_vis.values_list('title_of_post', 'date_of_post', 'intro_text', 'homepage_chart_image')).order_by('-date_of_post')

        other_data = DataVis.objects.filter(publish=True).filter(date_of_post__lte=timezone.now())[0:5]

        return data_vis, data_vis_int, other_data

    def get(self, request):
        """Gather data to return to the view."""
        # dict of data for.

        kwargs = {}
        data_vis, data_vis_int, other_data = self.get_queryset()

        if data_vis and data_vis_int and ((data_vis_int.date_of_post < data_vis.date_of_post) 
            or (data_vis_int.date_of_post == data_vis.date_of_post)):

            try:
                # Removes first bit of data - as it is the main post. 
                other_data = other_data[0:4]
            except:
                other_data = ""
        
            kwargs['data_vis_main'] = data_vis_int
            kwargs['other_posts'] = other_data
        
        elif data_vis and data_vis_int and data_vis_int.date_of_post > data_vis.date_of_post:
            
            try:
                # Removes first bit of data - as it is the main post. 
                other_data = other_data[1:5]
            except:
                other_data = ""

            kwargs['data_vis_main'] = data_vis
            kwargs['other_posts'] = other_data
        
        return render(request, self.template_name, kwargs)


    # def get(self, request):
    #     """Gather data to return to the view."""
    #     test = test_graph.draw()
    #     # dict of data for.
    #     kwargs = {'test1': test, 
    #         'test2': 'TEST2',
    #         'data_vis_list': self.get_queryset()}        
        
    #     return render(request, self.template_name, kwargs)


def data_vis_post(request, slug, pk):

    data = get_object_or_404(DataVis, pk=pk, slug=slug)
    type_of = data.template_to_use

    if data.publish == True:
        return render(request, f'data_vis/data_vis_page_{type_of}.html', {'datavis': data})
    else:
        raise Http404() 


def interactive_data_vis_page(request, slug, pk):    
    """
    """
    page = get_object_or_404(DataVisInteractive, pk=pk, slug=slug)
    bokeh_server_doc = server_document(f"{environ['BOKEH_URL']}/{page.bokeh_app_name}")
    
    # print("HERE----------------")
    # print(f"{environ['BOKEH_URL']}/{page.bokeh_app_name}")
    if page.publish == True:
        return render(request, 'data_vis/data_vis_interative_page.html', 
        {'datavisinteractive': page, 'bokeh_server_doc': bokeh_server_doc})
    else:
        raise(Http404)


def test_bokeh(self):
    #bk_script = 'bokeh serve --show test_bokeh_app/my_app.py --port 1555 --allow-websocket-origin=0.0.0.0:5001'
    #system(f"if ! lsof -i:1555 ; then {bk_script}; else echo bokeh running; fi &>-")
    test_bk = server_document(f"{environ['BOKEH_URL']}/plasmodium_gametocytes")
    return render(self, 'data_vis/test.html', {'test': test_bk})
  



"""
TODO
Want to have a page that is for returning data vis.
Have the code for making interactive charts with user data in the graphs module. 
"""




