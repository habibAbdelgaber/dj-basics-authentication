from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm


def home(request):
    return render(request, 'home.html')

def signin(request):
    form = LoginForm()
    # user = User.objects.get(username=username)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                    messages.success(request, 'You have logged in successfully')
            else:
                messages.info(request, 'Your account is disabled')
        else:
            messages.error(request, 'invalid username or password')

    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     try:
    #         user = User.objects.get(username=username)
    #         if user is not None:
    #             user = authenticate(username=username, password=password)
    #             if user.is_active:
    #                 login(request, user)
    #                 return redirect('/')
    #                 messages.success(request, 'You have logged in successfully!')
    #             else:
    #                 HttpResponse('Your account is disabled')

    #         else:
    #             HttpResponse('username does not exist!')
    #     except ValueError as e:
    #         raise e

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signin.html', context)


def signup(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, f'You have signed up {user.username} successfully')
            return redirect('signin')

    form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def signout(request):
    logout(request)
    return render(request, 'accounts/signout.html')
