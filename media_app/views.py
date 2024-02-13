from django.shortcuts import render
from .models import Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    images = Image.objects.all().order_by('id')
    paginator = Paginator(images, 4)
    page = request.GET.get('page')
    paged_images = paginator.get_page(page)
    image_number = images.count()
    context = {'photos': paged_images,
               'image_number': image_number}
    return render(request, 'index.html', context)
