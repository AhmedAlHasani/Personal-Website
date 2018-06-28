from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    #home page for the posts app
    path('', views.home, name='home'),
    path('projects/', views.projects, name = 'projects'),
    path('about/', views.about, name = 'about'),
    path('test/', views.test, name='test'),
 	path('projects/<int:project_id>', views.detail, name='detail'),
]