"""
11 - Data com mês por extenso.
Construa uma função que receba uma data no formato DD/MM/AAAA e
devolva uma string no formato D de mesPorExtenso de AAAA.

Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""

data = input('Digite um data na expressão dd/mm/yyyy ')

def mesPorExtenso(data):

    dia, mes, ano = map(int, data.split('/'))

    valida = False

    # Meses com 31 dias
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or \
            mes == 8 or mes == 10 or mes == 12):
        if (dia <= 31):
            valida = True

    # Meses com 30 dias
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if (dia <= 30):
            valida = True

    #se o mês for fevereiro, precisamos saber se ele é Bissexto
    elif mes == 2:
        # Testa se é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if (dia <= 29):
                valida = True
        elif (dia <= 28):
            valida = True

    meses = ['Janeiro',
             'Fevereiro',
             'Março',
             'Abril',
             'Maio',
             'Junho',
             'Julho',
             'Agosto',
             'Setembro',
             'Outubro',
             'Novembro',
             'Dezembro']

    if (valida):
        return 'Válida', meses[int(mes)-1]
    else:
        return 'NULL','NULL'

valida, mesExtenso = mesPorExtenso(data)

print(f'A data é: {valida}, Mês por Extenso: {mesExtenso}')