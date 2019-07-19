from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.dates import ArchiveIndexView 
from .views import *
from .models import DataVis as DVModel



app_name = "data_vis"

urlpatterns = [
    path('', DataVisHomepage.as_view(), name='data_vis'),
    path('<slug:slug>_<pk>/', DataVisPost.as_view(), name="data_vis_post"),
    path('archive/',
         ArchiveIndexView.as_view(model=DVModel, date_field="date_of_post"),
         name="data_vis_archive"),
   # path('', views.testpage, name='data_vis')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# alsa_output.pci-0000_1e_00.3.analog-stereo





