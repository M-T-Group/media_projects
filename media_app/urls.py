from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register')
]
