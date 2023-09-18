from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ContatoForm
from .utils import EnviarEmail
from django.contrib import messages
from django.urls import reverse
from .models import Post,TituloBlog
from django.utils.text import slugify

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = ContatoForm.recuperar_formulario()
        return render(request, self.template_name, {'form': form, 'errors': form.errors})
    
    def post(self, request, *args, **kwargs):
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()
            EnviarEmail.enviar_email(contato=contato)
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect(reverse('home_page')+ '#form', self.template_name, {'form': ContatoForm.recuperar_formulario()})
        else:
            return redirect(reverse('home_page')+ '#form',self.template_name, {'form': form, 'errors': form.errors})


class BlogPage(TemplateView):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        titulo_blog = TituloBlog.objects.last()
        context = {'posts':post,'titulo_blog':titulo_blog}
        return render(request, self.template_name,context)
    

class PostPage(TemplateView):
    template_name = 'single.html'

    def get(self, request, titulo, *args, **kwargs):
        # Normalize o título removendo espaços em branco extras e convertendo para minúsculas
        titulo_normalizado = slugify(titulo, allow_unicode=True)
        titulo_limpo = titulo_normalizado.replace('-',' ')
        post = get_object_or_404(Post, titulo__iexact=titulo_limpo)
        posts_sugestoes = Post.objects.exclude(id=post.id)

        context = {'item': post,'posts':posts_sugestoes}
        return render(request, self.template_name, context)