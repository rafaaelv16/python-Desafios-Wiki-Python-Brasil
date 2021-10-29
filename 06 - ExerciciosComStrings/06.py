"""
6 - Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e
imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""
import datetime
valida = False

ano_atual = datetime.date.today().year

while valida == False:
    data = input('Data Nascimento ')

    dia, mes, ano = map(int, data.split('/'))

    #vendo se a pessoa não tem mais de 150 anos
    if ((ano_atual - ano) > 0) & ((ano_atual - ano) < 150):
        valida = True

    if (valida == True) & (dia <= 31):
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
        print(f'Você nasceu em {dia} de {meses[mes-1]} de {ano}.')
    else:
        print('Data Inválida!Tente Novamente')
