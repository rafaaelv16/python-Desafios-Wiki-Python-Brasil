"""
7 - Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma
prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e
passar estes valores para a função valorPagamento, que calculará o valor a ser pago
e devolverá este valor ao programa que a chamou.

O programa deverá então exibir o valor a ser pago na tela.
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que
seja informado um valor igual a zero para a prestação.

Neste momento o programa deverá ser encerrado, exibindo o relatório do dia,
que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma.
Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

"""

#função pra calcular o total_prestacao
def valorPagamento(valorPrestacao, dias_atraso):
    #atribuindo o valor da prestação ao total, partindo do principio que dias de atraso será 0
    total_prestacao = valorPrestacao

    #se dias de atraso for maior ou igual a i fará o calculo dos juros
    if dias_atraso >= 1:
        total_prestacao += valorPrestacao * ((0.001 * dias_atraso) + 0.03)

    #valor que será retornado da função
    return total_prestacao

valor = -1
valor_total_prestacoes = prestacoes = 0

#enquanto valor da prestação for maior que zero, continue
while valor != 0:
    valor = -1
    dias_atrasados = -1
    while (valor < 0):
        valor = float(input('Valor da prestação.'))
        if (valor < 0):
            print('Valor Inválido. Tente novamente')

    if valor > 0:
        while (dias_atrasados < 0):
            dias_atrasados = float(input('Dias em atraso'))
            if (dias_atrasados < 0):
                print('Valor Inválido. Tente novamente')
        prestacoes += 1

    total = valorPagamento(valor,dias_atrasados)

    valor_total_prestacoes += total

    if total > 0:
        print(f'O valor a ser pago é: {total}')
    else:
        print('Você optou por encerrar o programa')


if prestacoes > 0:
    print(f"foram pagos {prestacoes} prestações e o valor total de prestações pagas no dia foi de {valor_total_prestacoes}")
else:
    print('Hoje não foi paga nenhuma prestação')