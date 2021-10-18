"""
Programa anterior
    Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor
    e a soma dos valores.

19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

qtd_numeros = int(input('Digite a quantidade de números a ser digitado: '))

menor = maior = soma = 0
numero = -1
for i in range(1, qtd_numeros+1):
    while (numero < 0) | (numero > 1000):
        numero = float(input(f'Digite o {i}º número. Entre 0 - 1000: '))
    if i == 1:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    soma += numero
    numero = -1

print(f"""A soma dos valores é: {soma}
O maior número é: {maior}
O menor número é: {menor}""")