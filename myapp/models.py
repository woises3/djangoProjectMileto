from django.db import models

# Create your models here.

class registro_Usuario(models.Model):
    email               = models.CharField(max_length=40)
    password            = models.CharField(max_length=40)
    inputAddress        = models.CharField(max_length=40)
    inputCity           = models.CharField(max_length=40)
    inputState          = models.CharField(max_length=40)
    inputZip            = models.CharField(max_length=40)
    inputRecuperacion   = models.CharField(max_length=40)

    def __str__(self):
        return f"Correo: {self.email} - Contraseña {self.password} - Direccion 1 {self.inputAddress} - Ciudad {self.inputCity} - Estado {self.inputState} - Codigo postal {self.inputZip} - Cod. Recuperacion {self.inputRecuperacion}"