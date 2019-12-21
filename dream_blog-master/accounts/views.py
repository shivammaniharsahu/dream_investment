
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, 'Login successfully you are ready to comment');
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        messages.success(request, 'Signup successfully you are ready to login');
        if next:
            return redirect(next)
        return redirect('/accounts/logout2/')
    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view2(request):
    logout(request)
    return redirect('/')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout  successfully');
    return redirect('/')
