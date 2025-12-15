from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import EmailAuthenticationForm, RegisterForm, UserPasswordUpdateForm
from dashboard.models import UserDetails


def register_view(request):
    from django.http import JsonResponse
    return JsonResponse({
        'message': 'Please use the API endpoint for registration',
        'endpoint': '/api/auth/users/register/',
        'method': 'POST',
        'required_fields': ['username', 'email', 'password']
    }, status=200)

def login_view(request):
    from django.http import JsonResponse
    return JsonResponse({
        'message': 'Please use the API endpoint for login',
        'endpoint': '/api/auth/users/login/',
        'method': 'POST',
        'required_fields': ['email', 'password']
    }, status=200)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, "Logout successful! You are now logged out.")
    return redirect('login') 

@login_required(login_url='login')
def update_password(request):
    if request.method == 'POST':
        form = UserPasswordUpdateForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been updated successfully!")
        else:
            messages.error(request, "There was an error updating your password. Please try again.")
    
    return redirect(reverse('home'))