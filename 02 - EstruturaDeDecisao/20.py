"""
20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

n1 = int(input('Digite a primeira nota'))
n2 = int(input('Digite a segunda nota'))
n3 = int(input('Digite a terceira nota'))

media = (n1 + n2 + n3) / 3
status = 'Reprovado'

if media >= 7:
    status = 'Aprovado'
if media == 10:
    status = 'Aprovado com Distinção'

print(f'{status} Média de: {media}')
