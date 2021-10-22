"""
2 - Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
"""
numero = zero_a_vinte_cinco = vinte_seis_a_cinquenta = cinquenta_um_a_setenta_cinco = setenta_seis_a_cem = 0
while numero >= 0:
    numero = int(input('Digite 0 para sair, Digite um valor: '))
    if numero < 0:
        print('Você digitou um número negativo. Saindo do Programa!')
    elif numero <= 25:
        zero_a_vinte_cinco += 1
    elif numero <= 50:
        vinte_seis_a_cinquenta += 1
    elif numero <= 75:
        cinquenta_um_a_setenta_cinco += 1
    elif numero <= 100:
        setenta_seis_a_cem += 1

print(f"""[0-25] foram digitados {zero_a_vinte_cinco} números,
[26-50] foram digitados {vinte_seis_a_cinquenta} números, 
[51-75] foram digitados {cinquenta_um_a_setenta_cinco} números
[76-100] foram digitados {setenta_seis_a_cem} números""")