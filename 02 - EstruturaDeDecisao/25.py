"""
25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação
    da pessoa no crime.

    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
    entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
    Caso contrário, ele será classificado como "Inocente".

"""

print('Faremos 5 perguntas, responda S para SIM e N para Não')

perguntas = ['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?','Devia para a vítima?','Já trabalhou com a vítima?']

positivos = 0

for i in perguntas:
    resposta = input(i)
    if resposta == 'S':
        positivos = positivos + 1

if positivos < 2:
    status = 'Inocente'
elif positivos == 2:
    status = 'Suspeita'
elif positivos <= 4:
    status = 'Cúmplice'
elif positivos == 5:
    status = 'Assassino'


print(status)





