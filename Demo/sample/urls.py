from django.urls import path
from .import views
 
urlpatterns=[
     path('', views.home, name="Sample-Home"),
     path('about/', views.about, name='Sample-About'),
 ]