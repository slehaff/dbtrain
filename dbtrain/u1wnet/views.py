from django.shortcuts import render

# Create your views here.
from .forms import Un1modelForm
from .models import Un1model

def u1net_detail_view(request):
    form = Un1modelForm(request.POST or None)
    obj = Un1model.objects.get(id=1)
    context = {
        'form': form
    }
    return render(request, 'u1wnet/u1net_detail.html', context)