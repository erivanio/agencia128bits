from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from website.forms import FormContato
from website.models import *

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
