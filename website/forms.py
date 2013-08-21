from django import forms
from django.core.mail import send_mail

class FormContato(forms.Form):
    nome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Digite seu nome'}))
    email = forms.EmailField(required=False)
    telefone = forms.CharField(max_length=10,required = False)
    mensagem = forms.Field(widget=forms.Textarea)

    def enviar(self):
        titulo = 'Mensagem enviada pelo site'
        destino = 'email@gmail.com'
        texto = """
        Nome: %(nome)s
        E-mail: %(email)s
        Telefone: %(telefone)s
        Mensagem: %(mensagem)s
        """ % self.cleaned_data

        send_mail(
            subject=titulo,
            message=texto,
            from_email=destino,
            recipient_list=[destino],
            )

