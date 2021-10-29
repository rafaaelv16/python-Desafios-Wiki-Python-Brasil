"""
4 - Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

nome = input('Digite seu nome: ')
palavra = ''
for i in range(0,len(nome)):
    palavra += nome[i]
    print(palavra)