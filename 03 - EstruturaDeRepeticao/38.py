"""
38 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
    percentual do ano anterior.
    Faça um programa que determine o salário atual desse funcionário.
    Após concluir isto,
    altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""
import datetime

ano_atual = datetime.date.today().year


def calcular_salario(salario):
    cont = 1
    for i in range(1996, ano_atual+1):
        if i == 1996:
            taxa = 1.5
        else:
            taxa *= 2
        aumento = salario * (taxa/100)
        salario += aumento
        print(f'Ano: {i} - ano: {cont} - Taxa: {taxa} - Aumento: {aumento} - Salário: {salario}')
        cont += 1

calcular_salario(1000)

salario = float(input('\n\nDigite o salário recebido em 1995: '))

calcular_salario(salario)