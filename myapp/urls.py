from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hombre/', views.hombre),
    path('mujer/', views.mujer),
    path('niños/', views.niños),
    path('descuentos/', views.descuentos),
    path('form1/', views.formulario_inicio_sesion),
]