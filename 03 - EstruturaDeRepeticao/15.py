"""
15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

N = int(input('Quantos números devem ter a sua sequencia de Fibonacci? '))

anterior = 0
proximo = 0

lista_vazia = []

for i in range(N):
    if (i < 2):
        lista_vazia.append(i)
    else:
        anterior = lista_vazia[-2]
        proximo = lista_vazia[-1] + anterior
        lista_vazia.append(proximo)

    if (i < (N-1)):
        print(lista_vazia[i], end=' ')
    else:
        print(lista_vazia[i])