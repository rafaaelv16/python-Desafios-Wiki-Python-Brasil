"""
44 - Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código.
    Os códigos utilizados são:
        1 , 2, 3, 4  - Votos para os respectivos candidatos
        (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
        5 - Voto Nulo
        6 - Voto em Branco

    Faça um programa que calcule e mostre:

    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;

    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos.

    Para finalizar o conjunto de votos tem-se o valor zero.

"""

print("""Vote e ajude a mudar a sociedade.
1 - José
2 - João
3 - Maria
4 - Josefa
5 - Nulo
6 - Branco""")

#conjunto = input('Digite o conjunto de votos separados por espaço. ').split()

conjunto = '1 2 3 5 6 6 5 1 2 1 7'.split()

qtde_votos = votos_nulos = votos_brancos = 0
#lista de candidatos com seu número, nome, quantidade de votos
candidatos = [[1,'José',0],
              [2,'João',0],
              [3,'Maria',0],
              [4,'Josefa',0],
              [5,'Nulo',0],
              [6,'Branco',0]]


for i in conjunto:
    n = int(i)
    for j in candidatos:
        if n == j[0]:
            qtde_votos += 1
            j[2] += 1

print("{:<15} {:<5}".format("Voto", "Quantidade"))
for i in candidatos:
    print("{:<15} {:<5}".format(i[1],i[2]))

    if i[0] == 5:
        votos_nulos = i[2]

    elif i[0] == 6:
        votos_brancos = i[2]

percentual_nulos = (votos_nulos / qtde_votos) * 100
percentual_brancos = (votos_brancos / qtde_votos) * 100

print(f'Votos nulos sobre total de votos(%): {percentual_nulos}\nVotos brancos sobre total de votos(%): {percentual_brancos}')