from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Theme


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                django_login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Логин или пароль введен неверно')

        return render(request, 'themes/login.html', {})


def logout(request):
    django_logout(request)
    return redirect('login')


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
