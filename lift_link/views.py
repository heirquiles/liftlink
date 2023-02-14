from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import NewPost, NewExercise, NewWorkout
from .forms import NewPostForm, ExerciseFormSet, NewExerciseForm, NewWorkoutForm
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
        form = NewPostForm(request.POST, request.FILES)
        
        if form.is_valid():
            body = form.cleaned_data['body']
            public = form.cleaned_data['public']
            image = form.cleaned_data['image']

            new_post = NewPost()
            new_post.body = body
            new_post.public = public
            new_post.image = image
            new_post.user = request.user
            new_post.save()

            return redirect('home')
    return render(request, 'lift_link/create.html', {'form': form})
@csrf_protect
def exercises(request):

    if request.method == 'POST':
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

            return redirect('workouts')
    context = {'form': form}
    return redirect(request, 'lift_link/workouts.html', context)
   
def workouts(request):
    
    if request.method == 'GET':
        workout = NewWorkoutForm()
    else:
        workout = NewWorkoutForm(request.POST)
    
        if workout.is_valid():
            title = workout.cleaned_data['title']
            new_workout = NewWorkout()
            new_workout.title = title
            new_workout.user = request.user
            new_workout.save()

            return render(request, 'lift_link/exercises.html')

    
    context = {'workout': workout}
    return render(request, 'lift_link/newWorkout.html', context)


def display_workouts(request):
    workouts = NewWorkout.objects.all()
    exercises = NewWorkout.exercises
    return render(request, 'lift_link/workouts.html', {'workouts': workouts, 'exercises': exercises})

def likes(request):
    id = int(request.POST.get('post_id'))
    post = get_object_or_404(NewPost, id=id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        
    else:
        post.likes.add(request.user)

    return redirect('home')