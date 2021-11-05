"""
5 - Classe Conta Corrente:

Crie uma classe para implementar uma conta corrente.

A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.

Os métodos são os seguintes: alterarNome, depósito e saque;

No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

"""

class ContaCorrente:
    def __init__(self,numeroConta,nomeCorrentista,saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self,nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if self.saldo < valor:
            print('Saldo Insuficiente')
        else:
            self.saldo -= valor

    def mostraConta(self):
        return self.numeroConta,self.nomeCorrentista,self.saldo


#Testes abaixo
cc = ContaCorrente(123456,'Rafa')
print(cc.mostraConta())
cc.alterarNome('jhow')
print(cc.mostraConta())
cc.depositar(1500)
print(cc.mostraConta())

cc.sacar(2000)
print(cc.mostraConta())