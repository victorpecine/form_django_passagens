from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens_app.classe_viagem import tipos_de_classe


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    data_ida = forms.DateField(label='Data de ida', widget=DatePicker())
    data_volta = forms.DateField(label='Data de volta', widget=DatePicker())
    # disable=True -> campo inalterável
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
    email = forms.EmailField(label='E-mail', max_length=150)
    informacoes = forms.CharField(label='Informações adicionais', max_length=200,
                                  widget=forms.Textarea(), required=False)
