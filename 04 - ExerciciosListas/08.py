"""
8 - Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

lista = []


for i in range(1,6):
    idade = altura = -1
    print(f"Dados da {i}ª pessoa: ")
    while (idade < 0) | (idade > 100):
        idade = int(input("Idade: "))
        if (idade < 0) | (idade > 100):
            print('Você digitou uma idade Inválida, tente novamente.')
        else:
            while (altura < 0) | (altura > 2.5):
                altura = float(input("Altura: "))
                if (altura < 0) | (altura > 2.5):
                    print('Você digitou uma altura inválida. Tente Novamente!')

    lista.append([idade,altura])

lista.reverse()

print(lista)

