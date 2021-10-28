"""
4 - Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’,se seu argumento for positivo,
e ‘N’, se seu argumento for zero ou negativo.
"""

def pos_neg(n1):
    if n1 >= 0:
        return 'P'
    else:
        return 'N'

print(pos_neg(-15))