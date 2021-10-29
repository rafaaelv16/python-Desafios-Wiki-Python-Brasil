"""
9 - Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado.

Por exemplo: 127 -> 721.
"""

n = int(input('Digite um número inteiro '))

def inverteNumero(numero):
    numero = str(numero)

    print(f'Invertendo o número {numero} -> {numero[::-1]}')

inverteNumero(n)