from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('home/', views.home, name='home'),
    path('newWorkout/', views.workouts, name='newWorkout'),
    path('workouts/', views.display_workouts, name='workouts'),
    path('exercises/', views.exercises, name='exercises'),
    path('exercise_list/<int:id>', views.exercise_list, name='exercise_list'),
    path('likes/<int:id>', views.likes, name='likes'),


]