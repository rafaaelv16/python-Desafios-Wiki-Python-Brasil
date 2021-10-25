"""
4 - Faça um Programa que leia um vetor de 10 caracteres,
e diga quantas consoantes foram lidas.

Imprima as consoantes.

"""

lista = input('Digite o vetor com 10 caracteres separados por espaço: ').upper().split()
consoantes = []
for i in lista:
    if i not in ('A','E','I','O','U'):
        consoantes.append(i)

print(f'Foram lidas {len(consoantes)} consoantes.\nForam elas:')
for i in consoantes:
    print(i)
