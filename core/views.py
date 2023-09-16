from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ContatoForm
from .utils import EnviarEmail
from django.contrib import messages
from django.urls import reverse

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


class TestePage(TemplateView):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)
    
    