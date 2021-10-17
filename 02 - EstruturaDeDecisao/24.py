"""
24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""

n1 = float(input('Digite um número'))
n2 = float(input('Digite outro número'))

operacao = 0
nome_operacao = ''
while (operacao < 1) | (operacao > 4):
    operacao = int(input("""Digite o tipo de operação:)
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    """))

if operacao == 1:
    result = n1 + n2
    nome_operacao = 'somar'

elif operacao == 2:
    result = n1 - n2
    nome_operacao = 'subtrair'

elif operacao == 3:
    result = n1 * n2
    nome_operacao = 'multiplicar'

elif operacao == 4:
    result = n1 / n2
    nome_operacao = 'dividir'


#par ou ímpar
par_impar = 'PAR'

if (result % 2 > 0):
    par_impar = 'ÍMPAR'


#positivo ou negativo
pos_neg = 'NEGATIVO'

if result >= 0:
    pos_neg = 'POSITIVO'


#decimal ou inteiro
decimal_inteiro = 'DECIMAL'

if (result == round(result)):
    decimal_inteiro = 'INTEIRO'

print(f"""Você optou por {nome_operacao} os números {n1} e {n2}
Obteve o resultado: {result}
Que é um número {par_impar}, {pos_neg}, {decimal_inteiro}""")