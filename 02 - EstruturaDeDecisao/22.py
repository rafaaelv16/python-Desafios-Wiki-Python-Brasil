"""
22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).

"""

n = int(input('Digite um número para saber se é par ou ímpar '))
status = 'PAR'

if (n % 2 > 0):
    status = 'ÍMPAR'

print(f'O número {n} é {status}')