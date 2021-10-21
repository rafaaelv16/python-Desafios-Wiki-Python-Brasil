"""
26 - Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

print("##  ELEIÇÕES 2022  ##")
eleitores = int(input('Quantos Eleitores são?\n'))
ze_geraldo = jonas_renan = janusa_costa = 0

for i in range(1,eleitores+1):
    voto = 0
    while voto not in (1,2,3):
        voto = int(input('Qual Candidato você escolhe: \n1 - Zé Geraldo;\n2 - Jonas Renan\n3 - Janusa Costa\n'))
        if voto not in (1,2,3):
            print('Voto inválido, tente novamente!')
    if voto == 1:
        ze_geraldo += 1
    elif voto == 2:
        jonas_renan += 1
    else:
        janusa_costa += 1

print(f'Canditato 1 - Zé Geraldo {ze_geraldo} votos'
      f'\nCanditato 2 - Jonas Renan {jonas_renan} votos'
      f'\nCanditato 3 - Janusa Costa {janusa_costa} votos')