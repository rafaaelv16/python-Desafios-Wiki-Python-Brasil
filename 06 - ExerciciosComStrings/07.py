"""7 - Conta espaços e vogais.
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),conte:

A - quantos espaços em branco existem na frase.
B - quantas vezes aparecem as vogais a, e, i, o, u.

"""
frase = input('Digite a frase: ')

print(f"A - quantos espaços em branco existem na frase: {frase.count(' ')}")
print(f"""B - quantas vezes aparecem as vogais
a: {frase.count('a') + frase.count('á') + frase.count('ã') + frase.count('â') + frase.count('à')}
e: {frase.count('e') + frase.count('é') + frase.count('ê')}
i: {frase.count('i') + frase.count('í')}
o: {frase.count('o') + frase.count('ó') + frase.count('ô')}
u: {frase.count('u') + frase.count('ú')}""")
