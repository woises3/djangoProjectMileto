from django.shortcuts import render
from django.shortcuts import get_list_or_404
from  django.http     import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def hombre(request):
    return render(request, 'hombre.html')
def mujer(request):
    return render(request, 'mujer.html')
def niños(request):
    return render(request, 'niños.html')
def descuentos(request):
    return render(request, 'descuentos.html')