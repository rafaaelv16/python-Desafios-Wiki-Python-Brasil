"""
Anterior:

4 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do
país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

5 - Altere o programa anterior permitindo ao usuário informar
as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""

import math
pop_a = pop_b = taxa_a = taxa_b = 0
while (pop_a >= pop_b):
    pop_a = int(input('Digite a população A: '))
    pop_b = int(input('Digite a população B: '))
    if (pop_a >= pop_b):
        print('Valores Inválidos. População A deve ser menor que população B')


while (taxa_a <= taxa_b) | (taxa_a > 100) | (taxa_a < 0) | (taxa_b > 100) | (taxa_b < 0):
    taxa_a = float(input('Qual a taxa de crescimento da População A? '))
    if (taxa_a > 100) | (taxa_a < 0):
        print('Valor da taxa A deve estar entre 1 - 100')
    else:
        taxa_b = float(input('Qual a taxa de crescimento da População B? '))
    if (taxa_b > 100) | (taxa_b < 0):
        print('Valor da taxa B deve estar entre 1 - 100')

    if (taxa_a < taxa_b) | (taxa_a == taxa_b):
        print('Valores Inválidos. Taxa de crescimento A deve ser maior que B')



anos = 0

print('Ano:    População A:    População B:')
while pop_a < pop_b:
    anos += 1

    pop_a = math.floor(pop_a + (pop_a * (taxa_a/100)))
    pop_b = math.floor(pop_b + (pop_b * (taxa_b/100)))

    print(f'{anos}  {pop_a}    {pop_b}')

print(f'Demorariam {anos} para que a População A fosse maior que a População B')