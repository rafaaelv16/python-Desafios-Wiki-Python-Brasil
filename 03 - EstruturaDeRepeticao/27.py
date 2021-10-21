"""
27 - Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""
qtde_turmas = int(input('Quantas turmas temos?'))

alunos = total_alunos = 0
for i in range(1,qtde_turmas+1):
    while (alunos <= 0) | (alunos > 40):
        alunos = int(input(f'Quantos alunos tem na Turma {i}: '))
        if (alunos <= 0) | (alunos > 40):
            print('As turmas não podem ter menos que 1 e mais de 40 alunos, tente novamente;')

    total_alunos += alunos
    alunos = 0

print(f'A média das turmas é de {total_alunos/qtde_turmas:.2f} alunos')
