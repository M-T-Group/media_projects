from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import AddPhotoForm

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

# Photo detail


def PhotoDetail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    related = Image.objects.exclude(id=image.id)
    context = {'image': image,
               'related': related}
    return render(request, 'photo-detail.html', context)


# Download image
def DownloadView(request, pk):
    result = Image.objects.get(id=pk)
    response = HttpResponse(
        result.photo, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{result.location}"'
    return response

# Delete image


def DeleteView(request, pk):
    image = Image.objects.get(id=pk)
    image.delete()
    return redirect('index')
# Video page


def Video(request):
    return render(request, 'videos.html')

# About page


def AboutView(request):
    return render(request, 'about.html')

# Contact page


def ContactView(request):
    return render(request, 'contact.html')

# Dashboard view


def DashboardView(request):
    page1 = 1
    images = Image.objects.all()
    context = {'images': images, 'page1': page1}
    return render(request, 'dashboard.html', context)

# Add photo form


def AddPhotoView(request):
    page2 = 2
    photoform = AddPhotoForm()
    if request.method == 'POST':
        photoform = AddPhotoForm(request.POST, request.FILES or None)
        if photoform.is_valid():
            photo = photoform.save(commit=False)
            photo.owner = request.user
            photo.save()
            messages.success(request, 'Photo Added Successfully..!')
            return redirect('dashboard')
        else:
            return redirect('addphoto')
    context = {'page2': page2,
               'photoform': photoform}

    return render(request, 'dashboard.html', context)

# Login Page


def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, 'Login Successfully..!')
        return redirect('dashboard')
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
