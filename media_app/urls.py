from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('photo-detail/<int:pk>/', views.PhotoDetail, name='detail'),
    path('Download/<int:pk>', views.DownloadView, name='download'),
    path('delete-photo/<int:pk>/', views.DeleteView, name='delete'),
    path("videos/", views.Video, name='video'),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
    path('logout/', views.LogoutView, name='logout'),
]
