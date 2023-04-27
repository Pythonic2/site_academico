from django.db import models

# Create your models here.

class ContatoCliente(models.Model):
    name  = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    phone = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.name

   
