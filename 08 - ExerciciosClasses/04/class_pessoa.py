"""
4 - Classe Pessoa:

Crie uma classe que modele uma pessoa:

    A - Atributos: nome, idade, peso e altura
    B - Métodos: Envelhercer, engordar, emagrecer, crescer.
    Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade
    dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,idade):
        if self.idade < 21:
            self.crescer(0.05*idade)
        self.idade += idade


    def engordar(self,peso):
        self.peso += peso

    def emagrecer(self,peso):
        self.peso -= peso

    def crescer(self,altura):
        self.altura += altura

    def mostraPessoa(self):
        return self.nome, self.idade,self.peso,self.altura

p = Pessoa('rafael',18,73,1.83)

print(p.mostraPessoa())

p.envelhecer(2)

print(p.mostraPessoa())

p.crescer(0.3)

print(p.mostraPessoa())

p.engordar(10)

print(p.mostraPessoa())