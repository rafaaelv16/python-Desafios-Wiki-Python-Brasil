"""
43 - O cardápio de uma lanchonete é o seguinte:
        Especificação   Código  Preço
        Cachorro Quente 100     R$ 1,20
        Bauru Simples   101     R$ 1,30
        Bauru com ovo   102     R$ 1,50
        Hambúrguer      103     R$ 1,20
        Cheeseburguer   104     R$ 1,30
        Refrigerante    105     R$ 1,00

    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
    Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
    Considere que o cliente deve informar quando o pedido deve ser encerrado.


"""
cardapio = (['Cachorro Quente', 100, 1.20],
            ['Bauru Simples', 101, 1.30],
            ['Bauru com ovo', 102, 1.50],
            ['Hambúrguer', 103, 1.20],
            ['Cheeseburguer', 104, 1.30],
            ['Refrigerante', 105, 1])

print("""Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00""")

sair = 1
pedido = []
total = 0
while sair != 0:
    codigo = int(input('Digite o código do produto: '))
    tem_no_cadapio = False

    # temo no cardápio?
    for i in cardapio:
        if codigo == i[1]:
            tem_no_cadapio = True
            qtde = int(input('Digite a quantidade: '))
            valor = qtde * i[2]
            pedido.append([i[0],i[1],i[2],qtde,valor])
            total += valor

    # se tem no cardápio, adicionamos ao pedido
    if tem_no_cadapio == False:
        print('Não Temos esse item no cardápio. Tente novamente.')


    sair = int(input('Para finalizar o pedido digite 0, para continuar digite outro caracter'))


print('Resumo do Pedido')
print ("{:<15} {:<15} {:<15} {:<15} {:<10}".format("Especificação", "Código", "Preço unit.", "Quantidade", "Subtotal"))
for i in pedido:
    print("{:<15} {:<15} {:<15} {:<15} {:<10}".format(i[0], i[1], i[2], i[3], i[4]))

print(f"""\nTotal geral do pedido: {total}""")