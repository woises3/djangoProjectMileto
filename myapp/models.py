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