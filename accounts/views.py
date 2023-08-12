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
                    error_message = "User not found"
            else:
                error_message = "Invalid login credentials"
        else:
            form = CustomAuthenticationForm()

        return render(request, 'accounts/login.html', {'form': form, 'error_message': error_message})
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request, 'accounts/signup.html')
    
    else:
        return redirect('/')
    



def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user:
            # Generate a temporary password
            temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.set_password(temp_password)
            user.save()

            # Send the temporary password to the user's email
            subject = 'Password Reset'
            message = f'Your new password: {temp_password}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('accounts/login')  # Redirect to your login page
        else:
            # Handle the case where the email doesn't match any user
            pass

    return render(request, 'accounts/forgot_password.html')