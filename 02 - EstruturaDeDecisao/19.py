"""
19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

"""
lista = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

for i in lista:
    #numero = input('Digite um número inteiro menor que 1000')
    numero = str(i)

    qtde_numeros = len(numero)

    extenso_unidades = 'unidade'
    extenso_dezenas = 'dezena'
    extenso_centenas = 'centena'

    if qtde_numeros == 1:
        unidade = int(numero[0:1])
        if unidade > 1:
            extenso_unidades = 'unidades'

        print(f'{numero} = {unidade} {extenso_unidades}')

    elif qtde_numeros == 2:
        unidade = int(numero[1:2])
        dezena = int(numero[0:1])

        if unidade > 1:
            extenso_unidades = 'unidades'

        if dezena > 1:
            extenso_dezenas = 'dezenas'

        if unidade == 0:
            print(f'{numero} = {dezena} {extenso_dezenas}')

        else:
            print(f'{numero} = {dezena} {extenso_dezenas} e {unidade} {extenso_unidades}')

    elif qtde_numeros == 3:
        unidade = int(numero[2:3])
        dezena = int(numero[1:2])
        centena = int(numero[0:1])

        if centena > 1:
            extenso_centenas = 'centenas'

        if unidade > 1:
            extenso_unidades = 'unidades'

        if dezena > 1:
            extenso_dezenas = 'dezenas'


        if unidade == dezena == 0:
            print(f'{numero} = {centena} {extenso_centenas}')

        elif (unidade == 0) | (dezena == 0):
            if (unidade == 0):
                print(f'{numero} = {centena} {extenso_centenas} e {dezena} {extenso_dezenas}')

            if (dezena == 0):
                print(f'{numero} = {centena} {extenso_centenas} e {unidade} {extenso_unidades}')

        else:
            print(f'{numero} = {centena} {extenso_centenas}, {dezena} {extenso_dezenas} e {unidade} {extenso_unidades}')