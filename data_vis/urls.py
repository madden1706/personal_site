from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls.static import static # To deploy. 
from . import views
from .views import DataVisHomepage, DataVisPost


app_name = "data_vis"

urlpatterns = [
    path('', views.DataVisHomepage.as_view(), name='data_vis'),
    path('<slug:slug>_<pk>/', views.DataVisPost.as_view(), name="data_vis_post"),
   # path('', views.testpage, name='data_vis')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




