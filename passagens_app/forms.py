from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens_app.classe_viagem import tipos_de_classe
from passagens_app.validation import *
from passagens_app.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    # disable=True -> campo inalterável

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'data_ida': 'Data de ida',
                  'data_volta': 'Data de volta',
                  'data_pesquisa': 'Data da pesquisa',
                  'informacoes': 'Informações',
                  'classe_viagem': 'Classe do voo'}
        widgets = {'data_ida': DatePicker(),
                   'data_volta': DatePicker()}

    # método de validação
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        lista_erros = {}
        campo_tem_numero(origem, 'origem', lista_erros)
        campo_tem_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']  # trazendo todos os campos exceto o nome
