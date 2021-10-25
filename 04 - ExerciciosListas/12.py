"""
12 - Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior
à média de altura desses alunos.
"""

lista = [[15,1.8],[16,1.5],[12,1.5],
         [16,1.9],[17,1.3],[13,1.8],
         [10,1.5],[14,1.2],[14,1.85],
         [11,1.55],[19,1.8],[19,1.5],
         [10,1],[11,1.2],[12,1.1],
         [11,2],[12,2],[12,1],
         [13,1.75],[14,1.65],[15,1.60],
         [10,1.5],[14,1.2],[14,1.85],
         [10,1],[11,1.2],[12,1.1],
         [20,1.5],[21,1.9],[22,2]]
contador = soma = 0

for i in lista:
    soma += i[1]

media = soma / len(lista)

for i in lista:
    if (i[0] > 13) & (i[1] < media):
        contador += 1

print(f'São um total de {contador} alunos com mais de 13 anos e com altura menor que a média({media:.2f} m)')