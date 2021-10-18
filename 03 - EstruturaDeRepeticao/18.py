"""
18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor
e a soma dos valores.
"""

qtd_numeros = int(input('Digite a quantidade de números a ser digitado: '))

menor = maior = soma = numero = 0

for i in range(1, qtd_numeros+1):
    numero = float(input(f'Digite o {i}º número: '))
    if i == 1:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    soma += numero

print(f"""A soma dos valores é: {soma}
O maior número é: {maior}
O menor número é: {menor}""")