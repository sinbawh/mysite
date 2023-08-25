from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomAuthenticationForm
from django.conf import settings
import random
import string
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import CustomUserCreationForm 
from django.contrib import messages

# Create your views here.

def login_view(request):
    
    if not request.user.is_authenticated:
        error_message = None

        if request.method == 'POST':
            form = CustomAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if user is not None:
                    login(request, user)
                    return redirect('/')  # Replace 'home' with your desired redirect URL
                else:
                    messages.add_message(request,messages.ERROR,'user not found')
            else:
                messages.add_message(request,messages.ERROR,'Wrong username or password , please try again')
        else:
            form = CustomAuthenticationForm()

        return render(request, 'accounts/login.html', {'form': form, 'error_message': error_message})
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


#signup
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                # Log the user in after registration
                return redirect('accounts:login')  # Replace with your desired redirect URL
            else:
                messages.add_message(request,messages.ERROR,'Invalid trying for creating account')
        else:
            
            form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})
    else:
        return redirect('/')
    



