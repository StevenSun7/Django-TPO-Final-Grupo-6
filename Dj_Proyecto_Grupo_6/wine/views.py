from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# Create your views here.
def index(request):
    if(request.GET.get('param')):
        param_uno = request.GET.get('param')
    else:
        param_uno='defecto'
    param_dos = request.GET.get('param2')
    
    context = {'param_uno':param_uno,
                'param_dos':param_dos,
                'hoy':datetime.now(),
                }
    
    return render(request,'wine/index.html',context)

def tintos(request):
    return render(request,'wine/tintos.html')

def blancos(request):
    return render(request,'wine/blancos.html')

def espumantes(request):
    return render(request,'wine/espumantes.html')

def contacto(request):
    return render(request,'wine/contacto.html')