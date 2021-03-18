def origem_destino_iguais(origem, destino, lista_erros):
    """ Verifica se origem e destino são iguais """
    if origem == destino:
        lista_erros['destino'] = ('Origem e destino não podem ser iguais')


def campo_tem_numero(valor_campo, nome_campo, lista_erros):
    """ Verifica de há dígitos numéricos """
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = ('Não inclua números neste campo')
