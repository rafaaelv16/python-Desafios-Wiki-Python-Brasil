"""
24 - Faça um programa que calcule o mostre a média aritmética de N notas.
"""

lista_notas = input('Digite as notas separando-as por espaço ').split()

soma = 0
for i in lista_notas:
    soma += int(i)

print(f'A média aritimétia é: {soma/len(lista_notas)}')
