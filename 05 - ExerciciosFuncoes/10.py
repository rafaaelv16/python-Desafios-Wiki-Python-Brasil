"""
10 - Jogo de Craps.

Faça um programa de implemente um jogo de Craps.

O jogador lança um par de dados, obtendo um valor entre 2 e 12.

Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.

Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.

Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".

Seu objetivo agora é continuar jogando os dados até tirar este número novamente.

Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

"""
import random

print('Jogo de Craps')
def lancarDados():
    print()
    dados = random.randint(1, 6)
    dados += random.randint(1, 6)
    return dados


partida = 'continua'
jogada = 0
numero_a_comparar = 0
while partida == 'continua':
    numero_obtido = lancarDados()
    print(f'Valor Obtido: {numero_obtido}')
    jogada += 1
    if jogada == 1:
        if numero_obtido in (7,11):
            print('Natural\nVocê ganhou a partida.')
            partida = 'encerra'
        elif numero_obtido in (2,3,12):
            print('Craps\nVocê perdeu a partida.')
            partida = 'encerra'
        else:
            print('Ponto\nA partida continua.')
            numero_a_comparar = numero_obtido

    else:
        print(f'Número a ser obtido: {numero_a_comparar}')
        if numero_obtido == 7:
            print("Você perdeu a partida pois tirou 7 depois da 1ª rodada")
            partida = 'encerra'

        elif numero_obtido == numero_a_comparar:
            print("Você venceu a partida! \nParabéns!")
            partida = 'encerra'

