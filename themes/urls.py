from django.urls import path

from . import views


app_name = 'themes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.theme, name='theme'),
    path('<int:pk>/content/', views.content, name='content'),
]