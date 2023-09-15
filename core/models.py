from django.db import models
from django.contrib.auth.models import User

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

   
class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
    video_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo