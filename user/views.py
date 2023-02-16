from django.shortcuts import render, redirect
from .forms import BaseForm as LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from lift_link.models import NewPost
from .models import Profile


def login(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            username_input = form.cleaned_data['username']
            password_input = form.cleaned_data['password']
            user = authenticate(request, username=username_input, password=password_input)
            if user is not None:
                user_login(request, user)
                previous_page = request.GET.get('next')

                if previous_page is not None:
                    return redirect('previous_page')
                else:
                    return redirect('profile')

    return render(request, 'user/login.html', {'form': form})

def logout(request):
    user_logout(request)
    return redirect('login')

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else: 
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']

            if password_confirmation == password:
                user = User()
                user.username = username
                user.email = email
                user.set_password(password)
                user.save()
                return redirect('profile')

    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request, id):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
        
    user = User.objects.get(id=id)
    profile = user.profile
    if request.method == "POST":
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            profile.follows.add(profile)
        elif action == "unfollow":
            profile.follows.remove(profile)
        profile.save()

    posts = NewPost.objects.filter(user=request.user).order_by('-created_date')
    context = {'posts': posts, 'profile': profile}
    return render(request, 'user/profile.html', context)

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "user/profile_list.html", {"profiles": profiles})

 