"""
6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor
a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

medias = []
for aluno in range(1,11):
    media = 0
    print(f'{aluno}º aluno')
    for bim in range(1,5):
        notas = -1
        while (notas < 0) | (notas > 10):
            notas = float(input(f"Digite a nota do {bim}º Bimestre "))
            if (notas < 0) | (notas > 10):
                print('Nota inválida. Tente novamente!')
            media += notas


    media = media / 4

    medias.append(media)


print(f'Quatidade de alunos com média maior que 7: {sum(i > 7 for i in medias)}')

