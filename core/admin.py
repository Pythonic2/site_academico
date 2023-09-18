from django.contrib import admin
from .models import ContatoCliente
# Register your models here.
from .models import Post, TituloBlog


admin.site.register(ContatoCliente)
admin.site.register(Post)
admin.site.register(TituloBlog)

