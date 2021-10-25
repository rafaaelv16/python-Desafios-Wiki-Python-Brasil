"""
2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista = input('Digite o vetor com 10 número reais separados por espaço: ').split()

lista.reverse()

for i in lista:
    print(i)