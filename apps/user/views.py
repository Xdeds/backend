from django.shortcuts import render
# Create your views here.
from apps.user.forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from apps.user.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

class CreateUserView(CreateView):
    template_name = 'signup.html'
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('signup')
    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data(**kwargs)
        return context
    
# def signup(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались!')
#             return HttpResponseRedirect(reverse('signin'))
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'signup.html', {'form':form})

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

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data = request.POST, instance = request.user, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse ('profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance = request.user)
    context = {'form':form}
    return render(request, 'profile.html', context)

class EmailVerification(TemplateView):
    template_name = 'verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email = kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code = code)
        if email_verification.exists():
            user.is_confirm_email = True
            user.save()
            return super(EmailVerification, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')