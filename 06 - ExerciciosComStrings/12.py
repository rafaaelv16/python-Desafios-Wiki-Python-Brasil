"""
12 - Valida e corrige número de telefone. Faça um programa que leia um número de telefone,
e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente.
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133

"""

print('Valida e corrige número de telefone')
valido = False

while not valido:
    numero = input('Telefone: ')

    if ('-' in numero) & (len(numero) in (8,9)):
        numero = numero.split('-')
        if len(numero[0]) == 3:
            p1 = '3' + numero[0]
        else:
            p1 = numero[0]
        p2 = numero[1]

        if (len(p1) == 4) & (len(p2) == 4):
            valido = True


    elif ('-' not in numero) & (len(numero) in (7,8)):
        if len(numero) == 7:
            p1 = numero[0:3]
            p2 = numero[3:7]
            print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
            p1 = '3' + numero[0:3]
        elif len(numero) == 8:
            p1 = numero[0:4]
            p2 = numero[4:8]
        valido = True
    if not valido:
        print('Telefone Inválido. Tente Novamente;')

print(f"""Telefone corrigido sem formatação: {p1+p2}
Telefone corrigido com formatação: {p1}-{p2}""")