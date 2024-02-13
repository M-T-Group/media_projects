from django.shortcuts import render, redirect
from .models import Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# Create your views here.

# Home Page


def index(request):
    images = Image.objects.all().order_by('id')
    paginator = Paginator(images, 4)
    page = request.GET.get('page')
    paged_images = paginator.get_page(page)
    image_number = images.count()
    context = {'photos': paged_images,
               'image_number': image_number}
    return render(request, 'index.html', context)

# Video page


# About page


# Contact page


# Login Page
def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, 'Login Successfully..!')
        return redirect('index')
    return render(request, 'accounts/login.html')

# Sign Up page


def RegisterView(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist..!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already exist..!')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                username=username, password=password1)
                user.save()
                messages.success(request, 'Registration Successfully..!')
                return redirect('login')
        else:
            messages.error(request, 'Password not matching..!')
            return redirect('register')
    return render(request, 'accounts/register.html')

# Logout


def LogoutView(request):
    logout(request)
    return redirect('index')
