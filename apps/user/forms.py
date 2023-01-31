from apps.user.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя', 'class':'login-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите фамилию', 'class':'login-input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя пользователя', 'class':'login-input'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'type':'email', 'placeholder':'Email', 'class':'login-input'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Введите пароль', 'class':'login-input'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Подтвердите пароль', 'class':'login-input'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя', 'class':'login-input'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','placeholder':'Введите пароль', 'class':'login-input'}))
    class Meta:
        model = User
        fields = ('username', 'password')