from django import forms
from core.models import ContatoCliente

class ContatoForm(forms.ModelForm):

    class Meta:
        model = ContatoCliente

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        ''' remove any labels here if desired
        '''
        super(ContatoForm, self).__init__(*args, **kwargs)
        # you can also remove labels of built-in model properties
        self.fields['name'].label = ''
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['id'] = 'name'
        self.fields['name'].widget.attrs['placeholder'] = 'Seu Nome'

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'exemplo@examplo.com'



        self.fields['message'].label = ''
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['id'] = 'message'
        self.fields['message'] = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type':'text', 'id': 'comentario','rows':5,'col':10,'placeholder':'Escreva sua menssagem...'}),label='')

        self.fields['phone'].label = ''
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['id'] = 'phone'
        self.fields['phone'].widget.attrs['placeholder'] = 'whatsapp'

    @classmethod
    def recuperar_formulario(cls):

        return ContatoForm
