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
