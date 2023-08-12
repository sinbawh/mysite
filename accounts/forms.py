from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.db.models import Q

class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            UserModel = get_user_model()

            try:
                user = UserModel.objects.get(Q(username=username) | Q(email=username))
            except UserModel.DoesNotExist:
                user = None

            if user is not None and user.check_password(password):
                self.user_cache = user
            else:
                raise forms.ValidationError("Invalid login credentials")
        return self.cleaned_data
