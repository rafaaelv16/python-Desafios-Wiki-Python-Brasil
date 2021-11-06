"""
Exercício anterior:

Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).

Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.

Escreva um pequeno programa que teste sua classe.


14 - Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
harry=funcionário("Harry",25000)
harry.aumentarSalario(10)
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
        print('Mostrar Nome')
        if self.verificarInstaciamentoObjeto():
            print(f'Nome: {self.nome}')

    def mostrarSalario(self):
        print('Mostrar Salário')
        if self.verificarInstaciamentoObjeto():
            print(f'Salário: R$ {self.salario}')

    def verificarInstaciamentoObjeto(self):
        if (hasattr(self, 'nome') & hasattr(self, 'salario')):
            return True
        else:
            print('Usuário não foi instanciado corretamente.')

    def aumentarSalario(self,percentual):
        print('Aumentar salário')
        if self.verificarInstaciamentoObjeto():
            self.salario += self.salario * percentual

f = Funcionario('15.5',1500)

f.mostrarNome()
f.mostrarSalario()
f.aumentarSalario(0.10)

f.mostrarSalario()
