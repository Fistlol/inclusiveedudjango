from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Theme


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/') 
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Логин или пароль введен неверно')

        return render(request, 'login/', {})


def logoutUser(request):
    logout(request)
    return redirect('login/')


@login_required(login_url='login')
def index(request):
    theme_objects = Theme.objects.all()
    return render(request, 'themes/index.html', {'theme_objects': theme_objects})


@login_required(login_url='login')
def theme(request, pk):
    theme_object = Theme.objects.get(pk=pk)
    theme_objects = Theme.objects.all()
    return render(request, 'themes/theme.html', {
            'theme_object': theme_object,
            'theme_objects': theme_objects,
        })
