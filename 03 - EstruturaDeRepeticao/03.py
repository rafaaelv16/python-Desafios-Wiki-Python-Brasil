"""
3 - Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""

nome = salario = sexo = estado_civil = ''
idade = salario = -1

#validando nome
while (nome == '') or (len(nome) < 3):
    nome = input('Digite o seu nome ')
    if len(nome) < 3:
        print('Digite um nome maior que 3 caractere')

#validando idade
while (idade < 0) | (idade > 150):
    idade = int(input('Digite a sua idade '))
    if (idade < 0) | (idade > 150):
        print('Idade deve estar entre 0 e 150')

#validando salário
while (salario < 0):
    salario = int(input('Digite o seu salário '))
    if salario < 0:
        print('Digite um valor maior que 0!') 

while sexo not in('F','M'):
    sexo = input('Digite o sexo: F ou M ').upper()
    if sexo not in('F','M'):
        print('Valor Inválido, escolha uma opção: F ou M')

while estado_civil not in('s', 'c', 'v', 'd'):
    estado_civil = input('Digite o seu estado Civil: S, C, V ou D ').lower()
    if estado_civil not in('s', 'c', 'v', 'd'):
        print('Valor Inválido, escolha uma opção: S, C, V ou D')



print(f"""INFORMAÇÕES VALIDADAS COM SUCESSO!
Nome: {nome}
Idade: {idade}
Salário: {salario}
Sexo: {sexo}
Estado Civil: {estado_civil}
""")

