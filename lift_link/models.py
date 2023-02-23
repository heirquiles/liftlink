from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewPost(models.Model):
    title = models.CharField(max_length=100, default='title')
    body = models.TextField()
    public = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images/", blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        return self.user.username + ' ' + self.title

class NewExercise(models.Model):
    name = models.CharField(max_length=100)
    reps = models.IntegerField()
    sets = models.IntegerField()
    weight = models.IntegerField(default=0)
    notes = models.CharField(max_length=240, blank=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default='Admin')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class NewWorkout(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=5)
    exercises = models.ManyToManyField(NewExercise, related_name='workouts')
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
