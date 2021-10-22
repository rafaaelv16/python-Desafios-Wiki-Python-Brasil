"""
37 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte
a cada um dos clientes da academia seu código,
sua altura e seu peso.

O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto,
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""
lista = []
codigo_cliente = 1
while codigo_cliente != 0:
    codigo_cliente = int(input('Digite o código do cliente '))
    if codigo_cliente != 0:
        altura = float(input('Digite a sua altura '))
        peso = float(input('Digite o seu peso '))
        lista.append([codigo_cliente, altura, peso])

alto = pesado = soma_peso = soma_altura = 0
baixo = leve = 200

for i in lista:
    soma_altura += i[1]
    soma_peso += i[2]

    #descobrindo o mais alto
    if i[1] > alto:
        alto = i[1]
        cod_alto = i[0]

    # descobrindo o mais baixo
    if i[1] < baixo:
        baixo = i[1]
        cod_baixo = i[0]

    # descobrindo o mais pesado
    if i[2] > pesado:
        pesado = i[2]
        cod_pesado = i[0]

    # descobrindo o mais leve
    if i[2] < leve:
        leve = i[2]
        cod_leve = i[0]

print(f"""Cliente mais alto, cód: {cod_alto} altura: {alto}
Cliente mais baixo, cód: {cod_baixo} altura: {baixo}
Cliente mais gordo, cód: {cod_pesado} peso: {pesado}
Cliente mais magro, cód: {cod_leve} peso: {leve}
Média altura: {soma_altura/len(lista)}
Média peso: {soma_peso/len(lista)}""")