"""
10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
compreendido por eles.
"""
maior = menor = n1 = n2 = 0

while n1 == n2:
    n1 = int(input('Digite um número inteiro'))
    n2 = int(input('Digite outro número inteiro'))
    if n1 == n2:
        print('Você digitou valores iguais, por favor, digite valores diferentes.')

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

for i in range(menor,(maior+1)):
    print(i)