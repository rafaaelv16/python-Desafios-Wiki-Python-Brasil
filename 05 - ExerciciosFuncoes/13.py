"""
13 - Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres
‘+’ , ‘−’ e ‘| ‘.

Esta função deve receber dois parâmetros, linhas e colunas,
sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da
faixa de forma elegante.
"""
def desenhaMoldura(lin,col):
    for i in range(1, lin+1):
        if (i == 1) | (i == lin):
            print("+",'-' * col,'+')
        else:
            print("|",' ' * col,'|')


coluna = linha = 0
while (coluna <= 0) | (coluna > 20):
    coluna = int(input('Quantidade de colunas'))
    if (coluna <= 0) | (coluna > 20):
        print('Digite um valor entre 1 e 20')
    else:
        while (linha <= 0) | (linha > 20):
            linha = int(input('Quantidade de linhas'))
            if (linha <= 0) | (linha > 20):
                print('Digite um valor entre 1 e 20')

desenhaMoldura(linha,coluna)