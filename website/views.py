from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from website.models import *
from django import forms
from django.core.mail import send_mail

class FormContato(forms.Form):
    nome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Digite seu nome'}))
    email = forms.EmailField(required=False)
    telefone = forms.CharField(max_length=10,required = False)
    mensagem = forms.Field(widget=forms.Textarea)

    def enviar(self):
        titulo = 'Mensagem enviada pelo site'
        destino = 'erivanio.vanin@gmail.com'
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


def home(request):
    colaborador = Equipe.objects.filter(publicar__exact=1)
    projeto = Trabalhos.objects.filter(publicar__exact=1)

    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            form.enviar()
            mostrar = 'Mensagem enviada!'
            form = FormContato()
            return redirect('/')
    else:
        form = FormContato()

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
