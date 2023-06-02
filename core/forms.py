from django.forms import ModelForm
from django.forms import Textarea, TextInput
from core.models import ContatoCliente


class CaixaDeTexto(Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.update({'class': kwargs.pop('_class','form-control')})
        super().__init__(*args, attrs=kwargs)
      
    

class InputComum(TextInput):
    '''
        Nesse input, posso colocar tanto Text, Email, Password, Date, Number,file ... entre outros
    '''
    def __init__(self, *args, **kwargs):
        kwargs.update({'class': kwargs.pop('_class','form-control')})
        super().__init__(*args, attrs=kwargs)
  

# Criando o Form aqui
class ContatoForm(ModelForm):
    class Meta:
        model = ContatoCliente
        fields = '__all__'
        widgets = {
            "message" : CaixaDeTexto(id='message'),
            "name": InputComum(type="text",id='name',placeholder='Seu Nome'),
            "email": InputComum(type="email",id='email',placeholder='Digite seu email'),
            "phone": InputComum(type="tel",id='phone',placeholder='11912345678'),
        }
    
     
    @classmethod
    def recuperar_formulario(cls):
        return ContatoForm
    