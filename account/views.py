from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm

from django.contrib.auth import views as auth_views, login as auth_login, logout
from django.contrib.auth.decorators import login_required

from django.views import generic
from django.urls import reverse_lazy
import re
from .forms import LoginForm, RegisterForm
# Create your views here.

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')
    # LOGIN_REDIRECT_URL = '/home/'
    # def post(self, request):
    #     return redirect('home')


def register(request):

    # resit_vaild = r'(\w|\d|-|_|\s)'
    if request.method == 'POST':
        reg = RegisterForm(request.POST)
        if reg.is_valid():
            reg.save()
            # print(request.POST)
            return redirect('login')
    else:
        reg = RegisterForm()
    context = {"form":reg}
    return render(request, 'account/register.html', context)

# @login_required('register')
def log_out(request):
    logout(request)
    return redirect('home')


def user_update(request, pk):
    if request.method == 'POST':
        reg = RegisterForm(request.POST, instance=request.user)
        if reg.is_valid():
            reg.save()
            return redirect('home')
    else:
        reg = RegisterForm(instance=request.user)
        context = {"form":reg}
    return render(request, 'account/register.html', context)

