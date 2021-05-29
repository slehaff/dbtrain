from django.shortcuts import render

# Create your views here.
from .forms import Un1modelForm
from .models import Un1model

from django.http import HttpResponse

def home(request):
    return HttpResponse('Home Page')

def about(request):
    return HttpResponse('About Page')

def contact(request):
    return HttpResponse('Contact Page')

def detail(request):
    return HttpResponse('Detail Page')

def u1net_detail_view(request):
    form = Un1modelForm(request.POST or None)
    if form.is_valid():
        form.save()
    # obj = Un1model.objects.get(id=1)
    context = {
        'form': form
    }
    return render(request, 'u1wnet/u1net_detail.html', context)