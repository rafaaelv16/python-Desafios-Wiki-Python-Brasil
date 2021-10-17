#7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Digite o primeiro número'))
n2 = float(input('Digite o segundo número'))
n3 = float(input('Digite o terceiro número'))

maior = n1
menor = n1

if (n2 > n3) & (n2 > n1):
    maior = n2

elif (n3 > n2) & (n3 > n1):
    maior = n3


if (n2 < n3) & (n2 < n1):
    menor = n2

elif (n3 < n2) & (n3 < n1):
    menor = n3

print(f"""O maior número é {maior}
e o menor número é {menor}""")