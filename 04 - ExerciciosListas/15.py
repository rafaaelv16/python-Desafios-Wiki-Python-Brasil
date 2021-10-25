"""
15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).

Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;

Calcule e mostre a soma dos valores;

Calcule e mostre a média dos valores;

Calcule e mostre a quantidade de valores acima da média calculada;

Calcule e mostre a quantidade de valores abaixo de sete;

Encerre o programa com uma mensagem;
"""
n = 0
notas = []
print('Digite um número negativo para sair.')
while (n >= 0) | (n > 10):
    n = float(input('Nota: '))
    if n > 10:
        print('Nota Inválida')
    elif n >= 0:
        notas.append(n)

print(f"Quantidade de valores que foram lidos: {len(notas)}")
print("Valores na ordem em que foram informados, um ao lado do outro: ", *notas, sep=' ')

#copiando a os valores de notas pra notas inverso
notas_inverso = notas

#invertendo a ordem da lista
notas_inverso.reverse()

print("Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro: ", *notas_inverso,sep='\n')

print("Calcule e mostre a soma dos valores;")

soma_extenso = 'Soma = '
soma = 0
for i in range(0,len(notas)):
    if i < (len(notas)-1):
        soma_extenso += f'{notas[i]} + '
    else:
        soma_extenso += f'{notas[i]} ='
    soma += notas[i]

print(soma_extenso,soma)

media = soma/len(notas)
print(f"""Calcule e mostre a média dos valores
Média = Soma / número de alunos
Média = {soma} / {len(notas)} => Média = {media:.2f}""")


print("Calcule e mostre a quantidade de valores acima da média calculada")

cont_acima_media = 0
for i in range(0,len(notas)):
    acima_media = 'Falso'
    if notas[i] > media:
        acima_media = 'Verdadeiro'
        cont_acima_media += 1

    print(f'{notas[i]} > {media} : {acima_media}')

print(f"{cont_acima_media} alunos ficaram acima da média")

print("Calcule e mostre a quantidade de valores abaixo de sete")

cont_abaixo_sete = 0
for i in range(0,len(notas)):
    abaixo_sete = 'Falso'
    if notas[i] < 7:
        abaixo_sete = 'Verdadeiro'
        cont_abaixo_sete += 1

    print(f'{notas[i]} < 7 : {abaixo_sete}')

print(f"{cont_abaixo_sete} alunos ficaram abaixo de 7")

print('Programa Encerrado.')
