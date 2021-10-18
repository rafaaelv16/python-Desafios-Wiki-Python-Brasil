"""
14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
e a quantidade de números impares.
"""
par = impar = 0
for i in range(1,11):
    n = int(input(f'Digite o {i}º número de 5 numeros: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Tivemos {par} números pares e {impar} números ímpares')