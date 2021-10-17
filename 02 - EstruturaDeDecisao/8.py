#8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

n1 = float(input('Digite o valor do Primeiro produto'))
n2 = float(input('Digite o valor do Segundo produto'))
n3 = float(input('Digite o valor do Terceiro produto'))

menor = 'Primeiro'

if (n2 < n3) & (n2 < n1):
    menor = 'Segundo'

elif (n3 < n2) & (n3 < n1):
    menor = 'Terceiro'

print(f'Você deve comprar o {menor} produto')