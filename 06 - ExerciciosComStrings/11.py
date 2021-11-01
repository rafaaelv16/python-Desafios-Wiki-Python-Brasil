# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:49:46 2021

@author: Rafael Castro


11 - Jogo de Forca. Desenvolva um jogo da forca. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!"""


import random

erros = 0    
acertou = False
palavra_certa = []    
lista_palavras = []
chutes = []

with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            lista_palavras.append(linha)
            

print('Jogo da Forca')
palavra = random.choice(lista_palavras).upper()

qtde_letras = len(palavra)

for i in palavra:
    palavra_certa.append('_')

print(*palavra_certa,sep = " ")

print(f'A palavra tem : {qtde_letras} letras')

while (erros < 6) & (acertou == False):
    
    letra = input('Digite uma letra: ').upper()
    
    if len(letra) != 1:    
        print('Por favor, digite uma letra por vez;')
    else:
        if letra not in chutes:   
            chutes.append(letra)
            if letra not in palavra:
                erros += 1
                print(f'Você errou pela {erros} vez. Tente de novo!')
            else:
                acertos = cont = 0
                
                for i in palavra:
                    if i == letra:
                        palavra_certa[cont] = letra
                        acertos +=1
                    cont += 1
                        
                print('A palavra é:', *palavra_certa,sep = " ")
                print()
            
            if "_" not in palavra_certa:
                acertou = True
        else:
            print('Letra repetida. Tente novamente')
        
if erros == 6:
    print('Você foi Enforcado')
else:
    print('Parabéns, Você Venceu.')



#lista.random(0,len(lista_palavras))

