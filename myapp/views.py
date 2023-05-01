from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from myapp.models import registro_Usuario, inicio_Sesion, recuperacion_Clave
from myapp.forms import formulario_registro_usuario, formulario_inicio_sesion, formulario_recuperacion_clave

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

"""def formulario_inicio_sesion(request):
    return render(request, 'form_inicio_sesion.html')"""

def formulario_inicio_sesion2(request):
    if request.method == "POST":
        miFormulario = formulario_inicio_sesion(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = inicio_Sesion(int(informacion['id']), (informacion['email']), (informacion['password']))
            curso.save()
            return render(request, "index.html")
    else:
         miFormulario = formulario_inicio_sesion()

    return render(request, "form_inicio_sesion.html", {"miFormulario": miFormulario})

"""def registroUsuario(request):
    return render(request, 'form_registro_usuario.html') """
"""def registroUsuario(request):
      if request.method == 'POST':
            curso = registro_Usuario((request.post['email']), (request.post['password']), (request.post['inputAddress']), (
                request.post['inputCity']), (request.post['inputState']), (request.post['inputZip']), (request.post['inputRecuperacion']))
            curso.save()
            return render(request, "form_inicio_sesion.html")
      return render(request,"form_registro_usuario.html")  """

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


"""def formulario_recuperacion(request):
    return render(request, 'form_recuperacion_clave.html')"""

def formulario_recuperacion(request):
    if request.method == "POST":
        miFormulario = formulario_recuperacion_clave(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = recuperacion_Clave(int(informacion['id']), (informacion['email']), (informacion['inputRecuperacion']))
            curso.save()
            return render(request, "form_inicio_sesion.html")
    else:
         miFormulario = formulario_recuperacion_clave()

    return render(request, "form_recuperacion_clave.html", {"miFormulario": miFormulario})
