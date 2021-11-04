"""
13 - Jogo da palavra embaralhada.

Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras
embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma
aleatoriamente.

O jogador terá seis tentativas para adivinhar a palavra.

Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
"""
import random
lista_palavras = []
palavra_embaralhada = ''
tentativa = 0
acertou = False
msg = "Você Perdeu"

#lendo o arquivo e guardando cada uma das linhas em uma lista
with open("..\palavras.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)

#sorteando uma palavra dentro da lista de palavras lidas
palavra = random.choice(lista_palavras).upper()

#função pra embaralhar palavra
def embaralha_palavra(palavra):
    nova_palavra = list(palavra)
    random.shuffle(nova_palavra)
    return ''.join(nova_palavra).upper()

#se caso a palavra embaralhada seja igual a palavra original vai embaralhar novamente.
while (palavra_embaralhada == palavra) | (palavra_embaralhada == ''):
    palavra_embaralhada = embaralha_palavra(palavra)

#imprimindo o cabeçalho do programa
print('Jogo da palavra embaralhada.')

#imprimindo a palavra embaralhada
print(f"Palavra Embaralhada: {palavra_embaralhada}")

#condição pra ver se a pessoa acertou e se ainda tem palpites
while (tentativa <6) & (not acertou):
    tentativa += 1
    n = input(f'{tentativa}º Palpite').upper()
    if palavra == n:
        msg = f"Você Venceu no {tentativa}º palpite."
        acertou = True

#imprimindo a palavra sem estar embaralhada
print("A palavra era:",palavra)

#imprimindo resultado
print(msg)