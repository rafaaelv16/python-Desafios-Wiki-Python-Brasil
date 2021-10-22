"""
39 - Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

#conjunto = input('Digite dez conjuntos com 2 valores: número do aluno e altura').split()
conjunto = [1,180,2,200,3,205,4,170,5,165]

lista = []
for i in range(0,10,2):
    lista.append([conjunto[i],conjunto[i+1]])

alto = 0
baixo = 200

for i in lista:

    #descobrindo o mais alto
    if i[1] > alto:
        alto = i[1]
        cod_alto = i[0]

    # descobrindo o mais baixo
    if i[1] < baixo:
        baixo = i[1]
        cod_baixo = i[0]

print(f"""Aluno mais alto: {cod_alto} com {alto} centímetros
Aluno mais baixo: {cod_baixo} com {baixo} centímetros""")




