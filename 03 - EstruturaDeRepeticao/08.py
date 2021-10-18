"""
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
soma = media = 0
for i in range(1,6):
    n = int(input(f'Digite o {i}º número de 5 numeros: '))
    soma += n

media = soma / 5

print(f'A soma é: {soma} e a média é: {media}')