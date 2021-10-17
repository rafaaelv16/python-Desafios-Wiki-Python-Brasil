#16 - Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import numpy as np


area = int(input('Qual o tamanho da área a ser pintada?'))
preco_lata = 80
litros_por_lata = 18
area_por_litro = 3

area_por_lata = area_por_litro * litros_por_lata
quantidade_de_latas = area / area_por_lata
arredondadas = np.ceil(quantidade_de_latas)

preco_total = arredondadas * preco_lata

print(f'Serão usadas {arredondadas:.0f} lata(s) de tinta(s) a um custo total de R$ {preco_total}')


