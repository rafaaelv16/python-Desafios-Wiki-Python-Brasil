#9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
n3 = int(input('Digite o terceiro número'))

lista = []

lista.append(n1)
lista.append(n2)
lista.append(n3)

print(sorted(lista, reverse=True))