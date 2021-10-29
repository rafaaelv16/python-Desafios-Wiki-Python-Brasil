"""8 - Palíndromo.
Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para
esquerda ou vice−versa.
Por exemplo: OSSO e OVO são palíndromos.

Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.

Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""

frase = input('Digite a frase')

#retirando os espaços da frase
frase = frase.replace(" ", "")

#invertendo a frase já sem espaços
fraseInvertida = frase[::-1]

#condição definindo se é ou não palíndromo
if frase == fraseInvertida:
    print('É palíndromo')
else:
    print('Não é palíndromo')