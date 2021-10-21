"""
31 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.

O programa deve então mostrar o total da compra
e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco.
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
A saída deve ser conforme o exemplo abaixo:

    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
    ...
"""
n = 1
soma = conta_produtos = 0
lista= []
while n != 0:
    n = float(input('Digite o valor do produto: '))
    if lista != 0:
        soma += n
        lista.append(n)

dinheiro = float(input('Valor Pago '))
for i in lista:
    conta_produtos += 1
    print(f"""Produto {conta_produtos}: R$ {i:.2f}""")

print(f'Total: R$ {soma:.2f}'
      f'\nDinheiro: R$ {dinheiro:.2f}'
      f'\nTroco: R$ {dinheiro-soma:.2f} ')