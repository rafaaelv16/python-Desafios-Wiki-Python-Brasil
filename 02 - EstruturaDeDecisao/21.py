"""
21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e
depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

"""
valor = 0
valor = int(input('Digite o valor a ser sacado '))

while (valor < 10) | (valor > 600):
    print('ATENÇÃO - Valor deve ser de R$ 10 a 600. Vamos tentar novamente?')
    valor = int(input('Digite o valor a ser sacado '))

cem = cinquenta = dez = cinco = um = 0

print('Será fornecido')
if (valor // 100 > 0):
    cem = valor // 100
    valor = valor % 100
    print(f'{cem} nota(s) de 100')

if (valor // 50 > 0):
    cinquenta = valor // 50
    valor = valor % 50
    print(f'{cinquenta} nota(s) de 50')

if (valor // 10 > 0):
    dez = valor // 10
    valor = valor % 10
    print(f'{dez} nota(s) de 10')

if (valor // 5 > 0):
    cinco = valor // 5
    valor = valor % 5
    print(f'{cinco} nota(s) de 5')

if (valor // 1 > 0):
    um = valor // 1
    valor = valor % 1
    print(f'{um} nota(s) de 1')

