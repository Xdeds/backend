from apps.user.models import User
from django import forms
from datetime import timedelta
import uuid
from apps.user.tasks import send_verification_email

from django.utils import timezone
from apps.user.models import EmailVerification
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

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        expiration = timezone.now() + timedelta(hours = 48)
        # record = EmailVerification.objects.create(
        #     code = uuid.uuid4(),
        #     user = user, 
        #     expiration=expiration
        # )
        # record.send_mail_verification()
        send_verification_email.delay(user.id)
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя', 'class':'login-input'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','placeholder':'Введите пароль', 'class':'login-input'}))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'palceholder':'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'palceholder':'Введите фамилию'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'palceholder':'Введите имя пользователя', 'readonly':True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'email' ,'palceholder':'Email'}))
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'image')