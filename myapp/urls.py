from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hombre/', views.hombre),
    path('mujer/', views.mujer),
    path('niños/', views.niños),
    path('descuentos/', views.descuentos),
    path('form_inicio/', views.formulario_inicio_sesion),
    path('form_registro/', views.registroUsuario),
    path('form_recuperacion/', views.formulario_recuperacion),
]
