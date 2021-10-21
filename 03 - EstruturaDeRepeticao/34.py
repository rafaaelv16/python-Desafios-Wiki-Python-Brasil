"""
34 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
"""
numero = int(input('Digite o valor e descubra se é primo'))

contador = 0
primo = 'não é primo'

for i in range(1,numero+1):
    if numero % i == 0:
        contador += 1

if contador == 2:
    primo = 'é primo'

print(f'O número {numero} {primo}')