"""
28 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

qtde_cds = int(input("Quantas CD's temos?"))
soma = 0

for i in range(1,qtde_cds+1):
    valor_cd = float(input(f'Quanto você pagou pelo CD {i}: '))
    soma += valor_cd
media = soma / qtde_cds
print(f'Total investido R$ {soma:.2f}\nValor médio do CD R$ {media:.2f}')