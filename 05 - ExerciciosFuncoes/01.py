"""1 - Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário.
Use uma função que receba um valor n inteiro e imprima até a n-ésima linha."""

numero = int(input('Digite o número.'))

def imprimir(n):

    for i in range(1,n+1):
        linha = ''
        for j in range(1,i+1):
            linha += str(i) + ' '
        print(linha)
imprimir(numero)