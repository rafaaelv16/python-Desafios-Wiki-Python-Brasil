"""
14 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a
2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e
5 como "Assassino".

Caso contrário, ele será classificado como "Inocente".
"""
perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?",
"Já trabalhou com a vítima?" ]
respostas = []
respostas_sim = 0
classificacao = 'Inocente'
for i in range(0,5):
    resposta = ''
    while resposta not in ('S','N'):
        resposta = input(perguntas[i]).upper()
        if resposta not in ('S','N'):
            print('Você deve escolher S ou N')
        else:
            respostas.append(resposta)
            if resposta == 'S':
                respostas_sim += 1

if respostas_sim == 5:
    classificacao = 'Assassino'
elif (respostas_sim == 4) | (respostas_sim == 3):
    classificacao = 'Cúmplice'
elif (respostas_sim == 2):
    classificacao = 'Suspeito'

print(f'Participação no crime {classificacao}')