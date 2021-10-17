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
#import do pacote que fará a interface gráfica
from PySimpleGUI import PySimpleGUI as sg

#Layout
#definindo o tema que será usado em nosso Layout
sg.theme('Reddit')

#criando um layou com 4 linhas
layout = [
    [sg.Text('Valor de A'),sg.Input(key='a',size=(5,1))],
    [sg.Text('Valor de B'),sg.Input(key='b',size=(5,1))],
    [sg.Text('Valor de V'),sg.Input(key='c',size=(5,1))],
    [sg.Button('Calcular')],
    [sg.Text('Resultado:'), sg.Text(size=(30,10), key='-OUTPUT-')],
]
#Janela
janela = sg.Window('Equação do Segundo Grau', layout)

#Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':

        a = int(valores['a'])
        b = int(valores['b'])
        c = int(valores['c'])

        if a == 0:
            resposta = 'Esta não é uma equação do segundo grau, PROGRAMA ENCERRADO!'
            print(resposta)



        else:
            if b == c == 0:
                resposta = f'Trata-se de uma incompleta apresenta os coeficientes b e c iguais a zero pois B e C = 0\nDelta é maior que 0, então a equação possui duas raizes reais\nSendo Xi = 0\nSendo xii = 0'
                print(resposta)

            #Trata-se de uma equação incompleta onde c = 0

            elif c == 0:
                x1 = 0

                x2 = abs(b) / a

                resposta = f"""Trata-se de uma equação incompleta pois c = 0
                      \nDelta é maior que 0, então a equação possui duas raizes reais
                      \nSendo Xi = {x1}
                      \nSendo xii = {x2}"""

                print(resposta)

            elif b == 0:

                x = math.sqrt(abs(c)/a)

                resposta = f"""Trata-se de uma equação incompleta pois b = 0
                      \nSendo Xi = {x}
                      \nSendo xii = -{x}"""

                print(resposta)


            #Trata-se de uma equação completa onde temos todos os valores de A B C
            else:
                delta = (b ** 2) - (4*a*c)

                if delta < 0:
                    resposta = f'Delta é igual a {delta}\nA equação não possui raizes reais, PROGRAMA ENCERRADO!'
                    print(resposta)

                elif delta == 0:
                    x = (-1*(b)) / (2 * a)
                    resposta = f"""Delta é igual a zero, portanto a equação possui apenas uma raiz
                          \nSendo X = {x}"""
                    print(resposta)

                else:
                    x1 = ((-1*(b)) + math.sqrt(delta)) / (2 * a)
                    x2 = ((-1*(b)) - math.sqrt(delta)) / (2 * a)

                    resposta = f"""Delta é igual a {delta}
                          \nDelta é maior que 0, então a equação possui duas raizes reais
                          \nSendo Xi = {x1}
                          \nSendo xii = {x2}"""
                    print(resposta)

        valores['-IN-'] = resposta
        janela['-OUTPUT-'].update(valores['-IN-'])