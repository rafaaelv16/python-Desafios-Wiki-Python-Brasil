"""
5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor.

Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.

Imprima os três vetores.
"""
lista_numeros = []
lista_pares = []
lista_impares = []

for i in range(1,21):
    numero = int(input(f'Digite o {i}º número'))
    lista_numeros.append(numero)

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Números: {lista_numeros}\nPares: {lista_pares}\nÍmpares: {lista_impares}')