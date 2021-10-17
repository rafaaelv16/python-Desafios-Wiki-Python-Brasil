#13 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

n = input('Digite um número que equivale ao dia da semana ')

dias_da_semana = {'1': 'Domingo',
                  '2': 'Segunda',
                  '3': 'Terça',
                  '4': 'Quarta',
                  '5': 'Quinta',
                  '6': 'Sexta',
                  '7': 'Sábado'}

if n in dias_da_semana:
    print(dias_da_semana[n])

else:
    print('Inválido!')

