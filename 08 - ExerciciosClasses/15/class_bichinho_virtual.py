"""

15 - Classe Bichinho Virtual++:

Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e
por quanto tempo ele brinca com o bichinho.

Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

"""

class BichinhoVirtual:
    def __init__(self,nome,fome,saude,idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = self.mostrarHumor()

    def alterarNome(self,nome):
        self.nome = nome

    def alterarFome(self,fome):
        self.fome = fome

    def alterarSaude(self,saude):
        self.saude = saude

    def alterarIdade(self,idade):
        self.idade = idade

    def mostrarNome(self):
        return self.nome

    def mostrarFome(self):
        return self.fome

    def mostrarSaude(self):
        return self.saude

    def mostrarIdade(self):
        return self.idade

    def mostrarHumor(self):
        return (self.fome + self.saude)/2

    def mostrarBichinhoVirtual(self):
        print(f"""Nome: {self.nome}
Fome: {self.fome}
Saúde: {self.saude}
Idade: {self.idade}
Humor: {self.humor}""")

    def darComida(self,quantidade):
        self.fome -= quantidade

    def brincar(self,tempo):
        self.humor += tempo



t = BichinhoVirtual('nome',15,15,20)

t.mostrarBichinhoVirtual()
t.alterarNome('Geral')
t.mostrarBichinhoVirtual()
t.alterarFome(90)
t.mostrarBichinhoVirtual()
t.alterarIdade(22)
t.mostrarBichinhoVirtual()
t.darComida(10)
t.mostrarBichinhoVirtual()
t.brincar(10)
t.mostrarBichinhoVirtual()
