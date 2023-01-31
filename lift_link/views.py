from django.shortcuts import render, redirect, get_object_or_404
from .models import NewPost
from .forms import NewPostForm
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


   

