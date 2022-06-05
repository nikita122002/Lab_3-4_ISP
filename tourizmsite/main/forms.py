from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control',"rows":10}))
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 =forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =forms.CharField(label='Подтверждение пароля',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username','email','password1','password2')

