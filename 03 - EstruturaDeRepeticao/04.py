"""
4 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do
país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

"""
import math

pop_a = 80000
pop_b = 200000

taxa_a = 3
taxa_b = 1.5

anos = 0

print('Ano:    População A:    População B:')
while pop_a < pop_b:
    anos += 1

    pop_a = math.floor(pop_a + (pop_a * (taxa_a/100)))
    pop_b = math.floor(pop_b + (pop_b * (taxa_b/100)))

    print(f'{anos}  {pop_a}    {pop_b}')

print(f'Demorariam {anos} para que a População A fosse maior que a População B')