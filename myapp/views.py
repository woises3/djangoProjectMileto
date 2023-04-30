from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from myapp.models import registro_Usuario
from myapp.forms import formulario_registro_usuario

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


def formulario_inicio_sesion(request):
    return render(request, 'form_inicio_sesion.html')


"""def registroUsuario(request):
    return render(request, 'form_registro_usuario.html') """

def registroUsuario(request):
    if request.method == "POST":
        miFormulario = formulario_registro_usuario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = registro_Usuario(int(informacion['id']), (informacion['email']), (informacion['password']), (informacion['inputAddress']), (
                informacion['inputCity']), (informacion['inputState']), (informacion['inputZip']), (informacion['inputRecuperacion']))
            curso.save()
            return render(request, "form_inicio_sesion.html")
    else:
         miFormulario = formulario_registro_usuario()
    
    return render(request, "form_registro_usuario.html", {"miFormulario": miFormulario})


def formulario_recuperacion(request):
    return render(request, 'form_recuperacion_clave.html')
