from django.urls import path, re_path
from . import views
from .views import DataVisHomepage


app_name = "data_vis"

urlpatterns = [
    path('', views.DataVisHomepage.as_view(), name='data_vis'),
   # path('', views.testpage, name='data_vis')
]




