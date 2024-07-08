from django.shortcuts import render
from .models import Nav

# Create your views here.
def index(request):
    nav_items = Nav.objects.all()
    context = {"nav_items": nav_items}
    return render (request, 'alumnos/index.html', context)

def quienesSomos(request):
    nav_items = Nav.objects.all()
    context = {"nav_items": nav_items}
    return render (request, 'alumnos/quienesSomos.html',context)

def servicios(request):
    nav_items = Nav.objects.all()
    context = {"nav_items": nav_items}
    return render (request, 'alumnos/servicios.html',context)