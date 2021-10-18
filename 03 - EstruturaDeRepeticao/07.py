"""
7 - Faça um programa que leia 5 números e informe o maior número.
"""
maior = 0
for i in range(1,6):
    n = int(input(f'Digite o {i}º número de 5 numeros: '))
    if n > maior:
        maior = n

print(f'O Maior número é: {maior}')


#n1 = int(input('Digite o primeiro número 5 numeros separados por vírgula'))


