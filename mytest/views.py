from django.shortcuts import render, get_object_or_404
from .models import PollingUnit

# Create your views here.

def polling_unit_result(request):
    unit = PollingUnit.objects.all()
    context = {
        'all_unit': unit,
    }
    return render(request, 'index.html', context)
