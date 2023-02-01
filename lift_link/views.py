from django.shortcuts import render, redirect, get_object_or_404
from .models import NewPost, NewExercise
from .forms import NewPostForm, NewExerciseForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'lift_link/index.html')

def home(request):
    posts = NewPost.objects.all().order_by('-created_date')
    return render(request, 'lift_link/home.html', {'posts': posts})

@login_required
def create(request):
    if request.method == 'GET':
        form = NewPostForm()

    else:
        form = NewPostForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            public = form.cleaned_data['public']

            new_post = NewPost()
            new_post.title = title
            new_post.body = body
            new_post.public = public
            new_post.user = request.user
            new_post.save()

            return redirect('home')
    return render(request, 'lift_link/create.html', {'form': form})

def exercise(request):
    if request.method == 'GET':
        form = NewExerciseForm()
    else: 
        form = NewExerciseForm(request.POST)

        if form.is_valid():
            
            name = form.cleaned_data['name']
            reps = form.cleaned_data['reps']
            sets = form.cleaned_data['sets']
            notes = form.cleaned_data['notes']

            new_exercise = NewExercise()
            new_exercise.name = name
            new_exercise.reps = reps
            new_exercise.sets = sets
            new_exercise.notes = notes
            new_exercise.user = request.user
            new_exercise.save()

            return redirect('home')
    return render(request, 'lift_link/workouts.html', {'form': form})
   
def workouts(request):
    workouts = NewExercise.objects.all().order_by('-created_date')
    return render(request, 'lift_link/workouts.html', {'exercises': exercises})
