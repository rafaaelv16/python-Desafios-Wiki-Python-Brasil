"8 - Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."

n = int(input('Digite um número inteiro '))

def contaDigitos(numero):
    numero = str(numero)

    print(f'O número {numero} tem {len(numero)} dígitos.')

contaDigitos(n)