from django import forms


class formulario_registro_usuario(forms.Form):
    id = forms.IntegerField()
    email = forms.CharField()
    password = forms.CharField()
    inputAddress = forms.CharField()
    inputCity = forms.CharField()
    inputState = forms.CharField()
    inputZip = forms.CharField()
    inputRecuperacion = forms.CharField()

class formulario_inicio_sesion(forms.Form):
    id = forms.IntegerField()
    email = forms.CharField()
    password = forms.CharField()

class formulario_recuperacion_clave(forms.Form):
    id = forms.IntegerField()
    email = forms.CharField()
    inputRecuperacion = forms.CharField()
