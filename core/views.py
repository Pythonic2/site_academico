from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import ContatoCliente
from .forms import ContatoForm
from .utils import EnviarEmail
# Create your views here.

    
class HomePage(TemplateView):
    template_name = 'index.html'
    def get(self,request):
        return render(request, 'index.html',{'form':ContatoForm.recuperar_formulario()})
    
    def post(self, request, *args, **kwargs):
       
        form = ContatoForm.recuperar_formulario()(request.POST)
        
        if form.is_valid():
            contato = form.save()
            nome  = form['name'].value()
            email = form['email'].value()
            phone = form['phone'].value()
            menssagem = form['message'].value()
            EnviarEmail.enviar_email(nome,email,phone,menssagem)
            return render(request, 'index.html',{'form':ContatoForm.recuperar_formulario()})
