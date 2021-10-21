"""
36 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado
pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7
"""

n = int(input('Digite o valor da tabuada: '))

fim = inicio = 0

while fim <= inicio:
    inicio = int(input('Digite de qual número a tabuada deve iniciar: '))
    fim = int(input('Digite de qual número a tabuada deve encerrar: '))
    if fim <= inicio:
        print('Digite o valor do início menor ao fim')

print(f'Tabuada de {n}, começando de {inicio} e terminando de {fim}')

for i in range(inicio,fim+1):
    print(f'    {n} X {i} = {n*i}')
