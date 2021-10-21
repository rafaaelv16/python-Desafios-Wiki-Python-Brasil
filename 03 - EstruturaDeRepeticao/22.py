"""
Programa Anterior
    Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
    Um número primo é aquele que é divisível somente por ele mesmo e por 1.

22 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
por quais número ele é divisível.
"""

numero = int(input('Digite o valor e descubra se é primo'))

contador = 0
divisiveis = []

primo = ''

for i in range(2,numero):
    if numero % i == 0:
        contador += 1
        divisiveis.append(i)
        primo = f'não é primo pois além de ser divisível por 1 e por ele mesmo, é divisível por{divisiveis}'

if contador == 2:
    primo = 'é primo'


print(f'O número {numero} {primo}')

