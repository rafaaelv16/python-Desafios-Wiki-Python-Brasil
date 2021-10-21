"""
23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido
pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para
encontrar os números primos. Serão avaliados o funcionamento,
o estilo e o número de testes (divisões) executados.
"""

numero = int(input('Digite o valor e descubra se é primo'))

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

print(f'Foram feitas {soma_divisoes} divisões! \nE descobertos {numeros_primos} números primos.')



