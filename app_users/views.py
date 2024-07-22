# global
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View

# local
from .forms import RegistrationForm


class Registration(View):
    def get(self, request):
        registration_form = RegistrationForm()
        context = {
            'registration_form': registration_form
        }
        return render(request, 'users/registration.html', context=context)

    def post(self, request):
        registrtaion_form = RegistrationForm(data=request.POST)
        if registrtaion_form.is_valid():
            registrtaion_form.save()
            return redirect('login')
        else:
            context = {
                'registration_form': registrtaion_form
            }
            return render(request, 'users/registration.html', context=context)


class Login(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'users/login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            account = login_form.get_user()
            login(request, account)
            return redirect('home')
        else:
            context = {
                'login_form': login_form
            }
            print('inavlid user')
            return render(request, 'users/login.html', context=context)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
