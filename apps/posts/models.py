from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length = 20)
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length = 70)
    autor = models.CharField(max_length = 30)
    categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to = 'imagenes_posts') #ver video 30:00


    def __str__(self):
        return self.titulo

