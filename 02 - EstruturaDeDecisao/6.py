# 6 - Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Digite o primeiro número'))
n2 = float(input('Digite o segundo número'))
n3 = float(input('Digite o terceiro número'))

maior = n1

if (n2 > n3) & (n2 > n1):
    maior = n2

elif (n3 > n2) & (n3 > n1):
    maior = n3

print(f'O maior número é {maior}')