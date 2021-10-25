"""
9 - Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

vetor = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for i in vetor:
    soma += (i*i)
print(soma)