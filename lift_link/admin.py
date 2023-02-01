from django.contrib import admin
from .models import NewPost, NewExercise, NewWorkout


admin.site.register(NewPost)
admin.site.register(NewExercise)
admin.site.register(NewWorkout)

