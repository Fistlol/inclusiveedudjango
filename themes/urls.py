from django.urls import path

from . import views


app_name = 'themes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.theme, name='theme'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]