"""
1 - Tamanho de strings.

Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento
e são iguais ou diferentes no conteúdo.


Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!

Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres

As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

"""

palavra1 = input('String 1: ')
palavra2 = input('String 2: ')

print(f'\nTamanho de "{palavra1}": {len(palavra1)} caracteres')
print(f'Tamanho de "{palavra2}": {len(palavra2)} caracteres')

if len(palavra1) == len(palavra2):
    print('\nAs duas strings são do mesmo tamanhos.')
else:
    print('\nAs duas strings são de tamanhos diferentes.')

if palavra1 == palavra2:
    print('As duas strings possuem conteúdo iguais.')
else:
    print('As duas strings possuem conteúdo diferente.')

