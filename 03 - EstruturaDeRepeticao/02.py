"""
2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

usuario = senha = status = ''

while (status == '') | (usuario == '') | (senha == ''):
    usuario = input('Digite o nome do Usuário').upper()
    senha = input('Digite a Senha').upper()

    if usuario == senha:
        print('Usuário e senha não podem ser iguais. Tente novamente.')
    else:
        status = 'Verdadeiro'
        print('Usuário e senha são diferentes.')