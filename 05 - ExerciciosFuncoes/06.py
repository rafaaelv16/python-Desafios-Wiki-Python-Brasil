"""
6 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros.

Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.

Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.

Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é
A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas
as vezes que desejar.
"""

def conversao(h):
    am_pm = 'A'
    if h > 12:
        h = hora - 12
        am_pm = 'P'
    return h, am_pm

def imprimir(h,m,ap):
    print(f'{h}:{m} {ap}')

p = 1
while p != '':
    hora = minuto = -1

    #validando a entrada de hora: 0 a 23
    while (hora < 0) | (hora > 23):
        hora = int(input('Digite a hora'))
        if (hora < 0) | (hora > 23):
            print('Por favor, digite uma hora válida: 0 - 23')

    while (minuto < 0) | (minuto > 59):
        minuto = int(input('Digite os minutos'))
        if (minuto < 0) | (minuto > 59):
            print('Por favor, digite minutos válidos: 0 - 59')

    hora, am_pm = conversao(hora)

    imprimir(hora,minuto,am_pm)