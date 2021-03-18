from django.shortcuts import render
from passagens_app.forms import Passagem_forms


def index(request):
    form = Passagem_forms()
    contexto = {'form': form}
    return render(request, 'index.html', contexto)
