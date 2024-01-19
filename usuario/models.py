from django.db import models
from django.contrib.auth.models import AbstractUser


class Cliente(AbstractUser): 
    email = models.EmailField(unique=True)
    oab = models.CharField(max_length=6)
    foto_perfil = models.ImageField(upload_to='profile', default='profile/anonymous-user.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Perfil(models.Model):
    user = models.OneToOneField('Cliente', on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='profile', default='profile/anonymous-user.jpg')