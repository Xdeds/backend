from django.shortcuts import render
# Create your views here.
from apps.user.forms import UserRegistrationForm, UserLoginForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'signin.html', {'form':form})
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# def signin(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data = request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username = username, password = password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect('/')
#     else:
#         form = UserLoginForm()
#     return render(request, 'signin.html', {'form':form})