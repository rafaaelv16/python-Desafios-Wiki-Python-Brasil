"""
23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""

n = float(input('Digite um número'))

status = 'DECIMAL'

if (n == round(n)):
    status = 'INTEIRO'

print(f'O número {n} é {status}')