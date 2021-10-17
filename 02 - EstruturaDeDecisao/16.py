"""
16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes
situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""
import math

print('### Resolvendo Equações do segundo Grau ###')

a = int(input('Digite o valor de A '))

if a == 0:
    print('Esta não é uma equação do segundo grau, PROGRAMA ENCERRADO!')

else:
    b = int(input('Digite o valor de B '))
    c = int(input('Digite o valor de C '))

    delta = (b ** 2) - (4*a*c)

    if delta < 0:
        print('A equação não possui raizes reais, PROGRAMA ENCERRADO!')

    elif delta == 0:
        x = (-1*(b)) / (2 * a)
        print(f'Delta é igual a zero, portanto a equação possui apenas uma raiz'
              f'Sendo X = {x}')

    else:
        restox1 = ((-1*(b)) + math.sqrt(delta)) % (2 * a)
        if restox1 == 0:
            x1 = ((-1*(b)) + math.sqrt(delta)) / (2 * a)
        else:
            numeradorx1 = ((-1*(b)) + math.sqrt(delta))
            denominadorx1 = (2 * a)

            denominador_comum = numeradorx1 * denominadorx1
            maior_divisor_comum = 1

            maior = numeradorx1
            if denominadorx1 > numeradorx1:
                maior = denominadorx1

            for i in range(1, maior):
                if ((denominadorx1 % i) == 0) & ((numeradorx1 % i) == 0):
                    maior_divisor_comum = i

            denominadorx1 = denominadorx1 / maior_divisor_comum
            numeradorx1 = numeradorx1 / maior_divisor_comum


            x1 = str(numeradorx1) + '/' + str(denominadorx1)



        restox2 = ((-1 * (b)) - math.sqrt(delta)) % (2 * a)

        if restox2 == 0:
            x2 = ((-1*(b)) - math.sqrt(delta)) / (2 * a)
        else:
            numeradorx2 = ((-1*(b)) - math.sqrt(delta))
            denominadorx2 = (2 * a)

            denominador_comum = numeradorx2 * denominadorx2
            maior_divisor_comum = 1

            maior = numeradorx2
            if denominadorx2 > numeradorx2:
                maior = denominadorx2

            for i in range(1,maior):
                if ((denominadorx2 % i) == 0) & ((numeradorx2 % i) == 0):
                    maior_divisor_comum = i

            denominadorx2 = denominadorx2 / maior_divisor_comum
            numeradorx2 = numeradorx2 / maior_divisor_comum

            x2 = str(numeradorx2) + '/' + str(denominadorx2)

        print(f'Delta é igual a {delta}'
              f'\nDelta é maior que 0, então a equação possui duas raizes reais'
              f'\nSendo Xi = {x1}'
              f'\nSendo xii = {x2}')