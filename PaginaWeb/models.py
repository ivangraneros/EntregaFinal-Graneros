from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Page(models.Model):
    titulo = models.CharField(max_length = 100)
    subtitulo = models.CharField(max_length = 100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='pages_images/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo



class UserAvatar(models.Model):
    nombre = models.CharField(max_length = 100, blank=True)
    apellido = models.CharField(max_length = 100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='useravatar')
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    bio =models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}{self.avatar}"


# sistema de mensajeria


class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    leido = models.BooleanField(default=False)


    def __str__(self):
        return f"De {self.emisor.username} para {self.receptor.username}"