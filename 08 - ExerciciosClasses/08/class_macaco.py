"""
8 - Classe Macaco:

Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos
comer(), verBucho() e digerir().

Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos
diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro.
É possível criar um macaco canibal?
"""

class Macaco:
    def __init__(self,nome):
        self.nome = nome
        self.bucho = []

    def comer(self,comida):
        #testar se comida tem atributo nome
        if (hasattr(comida, 'nome')):
            print('Macacos não são canibais')
        else:
            self.bucho.append(comida)
            self.verBucho()


    def verBucho(self):
        print('Coisas no Bucho/Estômago')
        for i in self.bucho:
            print(i)

    def digerir(self):
        print('bucho está vazio')
        self.verBucho()
        self.bucho = []

    def mostrarMacaco(self):
        return self.nome, self.bucho

m = Macaco()

m.comer('strogonoff')
m.comer('shark')
m.comer('Sucrillos')

print(m.mostrarMacaco())

m2 = Macaco('Ronaldo')

m.verBucho()

m.comer(m2)

m.verBucho()


