"""
5 - Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item antes do imposto.

A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def somaImposto(taxaImposto,custo):
    return ((taxaImposto/100)+1)*custo

print(f"{somaImposto(10, 110.15):.2f}")