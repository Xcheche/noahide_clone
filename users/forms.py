from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

from users.models import Profile

class UserForm(UserCreationForm):
    captcha = CaptchaField()
    
    email = forms.EmailField(required=True)  # Ensure email is required

class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'image','email']
