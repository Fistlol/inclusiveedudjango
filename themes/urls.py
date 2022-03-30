from django.urls import path

from . import views


app_name = 'themes'
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('', views.index, name='index'),
    path('<int:pk>/', views.theme, name='theme'),
]
