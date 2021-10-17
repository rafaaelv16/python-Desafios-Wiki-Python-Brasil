#18 -   Faça um programa que peça o tamanho de um arquivo para download (em MB)
#       e a velocidade de um link de Internet (em Mbps),
#       calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

import math

print('### Download ###')
tamanho_arquivo = float(input('Digite o tamanho do arquivo em MB'))
velocidade = float(input('Digite a velocidade da internet em Mbps'))

tempo_estimado = (tamanho_arquivo / velocidade) / 60
tempo_estimado = math.ceil(tempo_estimado)

print(f'Para baixar um arquivo de {tamanho_arquivo}MB com uma velocidade de Download de {velocidade} Mbps são necessários {tempo_estimado} minutos.')