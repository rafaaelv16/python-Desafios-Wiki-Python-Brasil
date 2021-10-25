"""
13 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

meses = ['1 - Janeiro',
         '2 - Fevereiro',
         '3 - Março',
         '4 - Abril',
         '5 - Maio',
         '6 - Junho',
         '7 - Julho',
         '8 - Agosto',
         '9 - Setembro',
         '10 - Outubro',
         '11 - Novembro',
         '12 - Dezembro']

lista_graus = []

for i in range(0,len(meses)):
    graus = float(input(f'Digite a temperatura do mês {meses[i]} em graus Celsius: '))
    lista_graus.append(graus)

media = sum(lista_graus) / len(lista_graus)

print(f'Ocoreram temperaturas maiores que a média anual {media:.2f} nos seguintes mesmes com as seguintes temperaturas')
print("{:<15} {:<10}".format("Mês","Temperatura (ºC)"))

for i in range(0,len(meses)):
    if lista_graus[i] > media:
        print("{:<15} {:<10}".format(meses[i],lista_graus[i]))
