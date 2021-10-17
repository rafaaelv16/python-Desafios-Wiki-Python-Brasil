# 10 - Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar
#   M-matutino ou
#   V-Vespertino ou
#   N- Noturno.
#
#   Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Digite o turno que você estuda: M-matutino ou V-Vespertino ou N- Noturno')
mensagem = 'Valor inválido!'

if turno == 'M':
    mensagem = 'Bom Dia!'

elif turno == 'V':
    mensagem = 'Boa Tarde!'

elif turno == 'N':
    mensagem = 'Boa Noite!'

print(mensagem)