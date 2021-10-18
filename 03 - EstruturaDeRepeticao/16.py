"""
16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.

"""

anterior = 0
proximo = 0 

lista_vazia = []
N = 50
for i in range(N):
    if (i < 2):
        lista_vazia.append(i)
    else:
        anterior = lista_vazia[-2]
        proximo = lista_vazia[-1] + anterior
        if proximo < 500:
            lista_vazia.append(proximo)

string = ''
for i in lista_vazia:
    if i == lista_vazia[-1]:
        string += str(i)
    else:
        string += str(i) + ','

print(string)