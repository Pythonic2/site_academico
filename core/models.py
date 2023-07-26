from django.db import models

# Create your models here.

class ContatoCliente(models.Model):
    name  = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    phone = models.CharField(max_length=11)
    OPCOES_CUIDADOR = (
        ('Preciso de um Cuidador', 'Preciso de um cuidador'),
        ('Sou um Cuidador', 'Sou um cuidador'),
    )
    tipo = models.CharField(max_length=25, choices=OPCOES_CUIDADOR, default='')

    def __str__(self) -> str:
        return self.name

   
