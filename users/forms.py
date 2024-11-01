from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class CustomAuthenticationForm(AuthenticationForm):
    pass