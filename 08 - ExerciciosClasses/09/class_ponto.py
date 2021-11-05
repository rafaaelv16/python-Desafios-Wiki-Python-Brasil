"""9 - Classe Ponto e Retangulo:
Faça um programa completo utilizando funções e classes que:

    A - Possua uma classe chamada Ponto, com os atributos x e y.
    B - Possua uma classe chamada Retangulo, com os atributos largura e altura.
    C - Possua uma função para imprimir os valores da classe Ponto
    D - Possua uma função para encontrar o centro de um Retângulo.
    E - Você deve criar alguns objetos da classe Retangulo.
    #F - Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
    G - A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
    H - O valor do centro do objeto deve ser mostrado na tela
    I - Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo."""

class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.verticePartida = [0,0]

    def imprimirPontos(self):
        print('X: ', self.x)
        print('Y: ', self.y)
