#4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra')
vogais = 'aeiou'

if letra in vogais:
    print('É uma vogal!')
else:
    print('É uma consoante!')