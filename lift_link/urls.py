from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('home/', views.home, name='home'),
    path('workouts/', views.exercise, name='workouts'),


]