"""
32 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
"""

numero = int(input('Digite um número e descubra o seu Fatorial '))
soma=1
string = f'{numero}! = '

for i in range(1,numero+1):
    if i < numero:
        string += f' {i} .'
    else:
        string += f' {i} = '
    soma *= i

print(f'{string} {soma}')
