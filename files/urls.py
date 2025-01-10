from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_file, name='add_file'),  
    path('search/', views.search_file, name='search_file'), 
]
