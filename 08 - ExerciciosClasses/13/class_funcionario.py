"""
13 - Classe Funcionário:

Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).

Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.

Escreva um pequeno programa que teste sua classe.
"""

class Funcionario:
    def __init__(self,nome,salario):
        if (type(nome) != str) | ((type(salario) != float) & (type(salario) != int)):
            if (type(nome) != str):
                print('Nome deve ser do tipo string')
            if ((type(salario) != float) & (type(salario) != int)):
                print('Salario deve ser tipo float')
        else:
            self.nome = nome
            self.salario = salario
            print('Objeto instanciado')

    def mostrarNome(self):
        if self.verificarInstaciamentoObjeto():
            print(f'Nome: {self.nome}')
        else:
            print('Usuário não foi instanciado corretamente. Por isso, não foi possível mostrar o nome')

    def mostrarSalario(self):
        if self.verificarInstaciamentoObjeto():
            print(f'Salário: R$ {self.salario}')
        else:
            print('Usuário não foi instanciado corretamente. Por isso, não foi possível mostrar o salário')

    def verificarInstaciamentoObjeto(self):
        if (hasattr(self, 'nome') & hasattr(self, 'salario')):
            return True

f = Funcionario('15.5',15)

f.mostrarNome()
f.mostrarSalario()