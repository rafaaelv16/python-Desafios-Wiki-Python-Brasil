"""
14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0        A
    Entre 7.5 e 9.0         B
    Entre 6.0 e 7.5         C
    Entre 4.0 e 6.0         D
    Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

"""

n1 = float(input('Digite a primeira nota, valor de 0 a 10 '))
while (n1 < 0) | (n1 > 10):
    print('Ops, parece que você digitou um valor inválido! Vamos tentar novamente.')
    n1 = float(input('Digite a primeira nota, valor de 0 a 10 '))

n2 = float(input('Digite a segunda nota, valor de 0 a 10 '))
while (n2 < 0) | (n2 > 10):
    print('Ops, parece que você digitou um valor inválido! Vamos tentar novamente.')
    n2 = float(input('Digite a segunda nota, valor de 0 a 10 '))

media = (n1 + n2) / 2
status = 'APROVADO'

if media < 4:
    nota = 'E'
    status = 'REPROVADO'

elif (media < 6):
    nota = 'D'
    status = 'REPROVADO'

elif (media < 7.5):
    nota = 'C'

elif (media < 9):
    nota = 'B'

else:
    nota = 'A'

print(f"""Sua primeira nota foi: {n1}
Sua segunda nota foi: {n2}
Sua média foi: {media}
Seu conceito foi {nota}
Você foi: {status}""")