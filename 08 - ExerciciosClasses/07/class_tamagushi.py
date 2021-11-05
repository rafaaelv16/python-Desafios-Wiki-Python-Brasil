"""
7 - Classe Bichinho Virtual:

Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

    A - Atributos: Nome, Fome, Saúde e Idade
    b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade

    Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
    este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um
    atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

"""
class Tamagushi:
    def __init__(self,nome,fome,saude,idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

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

    def mostrarTamagushi(self):
        print(f"""Nome: {self.nome}
Fome: {self.fome}
Saúde: {self.saude}
Idade: {self.idade}
Humor: {self.mostrarHumor()}""")
t = Tamagushi('nome',15,15,20)

t.mostrarTamagushi()
t.alterarNome('Geral')
t.mostrarTamagushi()
t.alterarFome(90)
t.mostrarTamagushi()
t.alterarIdade(22)
t.mostrarTamagushi()

