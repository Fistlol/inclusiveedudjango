from django.shortcuts import render

from django.http import HttpResponse

from .models import Theme


def index(request):
    theme_objects = Theme.objects.all()
    return render(request, 'themes/index.html', {'theme_objects': theme_objects})


def theme(request, pk):
    theme_object = Theme.objects.get(pk=pk)
    theme_objects = Theme.objects.all()
    return render(request, 'themes/theme.html', {
            'theme_object': theme_object,
            'theme_objects': theme_objects,
        })


def content(request, pk):
    theme_object = Theme.objects.get(pk=pk)
    theme_objects = Theme.objects.all()
    return render(request, 'themes/content.html', {
            'theme_object': theme_object,
            'theme_objects': theme_objects,
        })