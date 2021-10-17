#17 - Faça um Programa que peça um número correspondente a um determinado ano e
# em seguida informe se este ano é ou não bissexto.

ano = int(input('Digite o ano a ser verificado'))
status = 'não é Bissexto'

if (ano % 4 == 0):
    if (ano % 100 == 0):
        if (ano % 400 == 0):
            status = 'é Bissexto'
    else:
        status = 'é Bissexto'

print(f'O ano {ano} {status}')
