from django.urls import path, re_path
from . import views
from django.conf.urls import handler404, handler500


app_name = "homepage"


urlpatterns = [
    path('', views.homepage, name='homepage'),
    #path('newpage/', views.newpage, name='newpage'),
    path('testpage/', views.testpage, name='testpage'),
    path('contact/', views.contact, name='contact'),
    path('about-me/', views.about_me, name='aboutme')

]

handler404 = "homepage.views.custom_404"
handler500 = "homepage.views.custom_500"