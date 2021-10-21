"""
35 - Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro
informado pelo usuário.
"""

numero = int(input('Digite o valor '))

contador = soma_divisoes = numeros_primos = 0

print(f'De 1 a {numero}. São primos: ')
for j in range(1,numero+1):
    for i in range(1, j+1):
        soma_divisoes += 1
        if j > 1:
            if j % i == 0:
                contador += 1
    if contador == 2:
        print(f'{j}')
        numeros_primos += 1

    contador = 0