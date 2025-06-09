from django import forms
from .models import Page, UserAvatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['titulo','subtitulo','contenido','imagen']



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password', 'password2']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAvatar
        fields = ['avatar', 'bio', 'birthdate']