from django import forms
from .models import Page, UserAvatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['titulo','subtitulo','contenido','imagen', 'autor']



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAvatar
        fields = ['nombre','apellido','avatar', 'bio', 'birthdate']
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'}),
        }