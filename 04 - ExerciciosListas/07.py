"""
7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre
    a soma,
    a multiplicação e
    os números.
"""

numeros = input('Digite o vetor com 5 número separados por espaço: ').split()

soma = 0
multiplicacao = 1

for i in numeros:
    multiplicacao *= int(i)
    soma += int(i)

print(f'Soma: {soma}\nMultiplicação: {multiplicacao}\n{numeros}')