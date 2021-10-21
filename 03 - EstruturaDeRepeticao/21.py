"""
21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

numero = int(input('Digite o valor e descubra se é primo'))

contador = 0
primo = 'não é primo'

for i in range(2,numero+1):
    if numero % i == 0:
        contador += 1

if contador == 1:
    primo = 'é primo'

print(f'O número {numero} {primo}')

