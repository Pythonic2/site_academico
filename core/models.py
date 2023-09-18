from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class ContatoCliente(models.Model):
    name  = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    phone = models.CharField(max_length=11)
    OPCOES_CUIDADOR = (
        ('Nao Selecionado', '--------'),
        ('Preciso de um Cuidador', 'Preciso de um cuidador'),
        ('Sou um Cuidador', 'Sou um cuidador'),
    )
    tipo = models.CharField(max_length=25, choices=OPCOES_CUIDADOR, default='')

    OPCOES_CIDADE = (
        ('Nao Selecionado', '--------'),
        ('João Pessoa', 'João Pessoa'),
        ('Campina Grande', 'Campina Grande'),
    )
    cidade = models.CharField(max_length=25, choices=OPCOES_CIDADE, default='')

    def __str__(self) -> str:
        return self.name

   
class TituloBlog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400, blank=True)
    imagem = models.ImageField() #540x540

    def __str__(self):
        return self.titulo
    
class Post(models.Model):
    autor = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    texto = RichTextUploadingField()
    imagem_post = models.ImageField(blank=True) #1534x2300
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo