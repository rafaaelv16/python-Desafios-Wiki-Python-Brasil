"""
45 - Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar
com o gabarito da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa).

Após cada aluno utilizar o sistema deve ser feita uma pergunta
se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.
    Gabarito da Prova:

    01 - A
    02 - B
    03 - C
    04 - D
    05 - E
    06 - E
    07 - D
    08 - C
    09 - B
    10 - A

    Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

"""
#Caso o gabarito já entre sem o input do professor
#gabarito = ["A","B","C","D","E","E","D","C","B","A"]

#Caso o gabarito seja inputdo pelo professor:
gabarito = []
numero_da_questao = 0
for i in range(1,11):
    numero_da_questao += 1
    questao = input(f'Digite o gabarito da questão {numero_da_questao}: ').upper()
    gabarito.append(questao)

print(gabarito)
print("\n" * 130)

qtde_questoes = 10

sair = 1
conta_alunos = maior_nota = soma_notas = media = 0
menor_nota = 10
aluno_maior_nota = aluno_menor_nota = ''
notas = []
while sair != 0:
    conta_alunos += 1
    acertos = 0
    nome = input('Digite o nome do aluno ')
    for i in range(0,qtde_questoes):
        resposta = input(f'Resposta da {i+1}ª questão: ').upper()
        if resposta == gabarito[i]:
            acertos += 1

    if acertos > maior_nota:
        maior_nota = acertos
        aluno_maior_nota = nome

    if acertos < menor_nota:
        menor_nota = acertos
        aluno_menor_nota = nome

    soma_notas += acertos

    sair = int(input('Se deseja sair digite 0; se tem outro aluno digite outro número'))

media = soma_notas / (conta_alunos)
print(f"""Maior nota: {maior_nota} do(a) aluno(a): {aluno_maior_nota}
Menor nota: {menor_nota} do(a) aluno(a): {aluno_menor_nota}
Total de alunos: {conta_alunos}
media: {media}
Confira abaixo o gabarito""")

numero_da_questao = 0
for i in gabarito:
    numero_da_questao += 1
    print(f'{numero_da_questao} - {i}')


