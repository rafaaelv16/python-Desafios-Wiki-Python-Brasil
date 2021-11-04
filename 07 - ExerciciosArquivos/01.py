"""
1 - Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,

contendo um relatório dos endereços IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""

lista_endereços = []
ips_validos = []
ips_invalidos = []

#lendo o arquivo e guardando cada uma das linhas em uma lista
with open("ips.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        lista_endereços.append(linha)

def validar_ips(ips):
    valida = True
    if '.' in ips:
        lista_ips = ips.split('.')
        for fracao_ip in lista_ips:
            if (int(fracao_ip) > 255) | (int(fracao_ip) < 0):
                valida = False
                break

    if valida:
        ips_validos.append(ips)
    else:
        ips_invalidos.append(ips)


for ips in lista_endereços:
    validar_ips(ips)


#limpando o arquivo
open('ips_validos_invalidos.txt', 'w').close()

#criando o arquivo, que receberá append(adições)
with open('ips_validos_invalidos.txt', 'a',encoding="utf-8") as arquivo:

    print("[Endereços válidos:]", file=arquivo)
    for i in ips_validos:
        print(i, file=arquivo)

    print("[Endereços Inválidos:]", file=arquivo)
    for i in ips_invalidos:
        print(i, file=arquivo)