"""
16 - Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos
do objeto.

Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu,
for informada na escolha do usuário.

Dica: acrescente um método especial str() à classe Bichinho.
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
        self.alterarHumor()

    def alterarSaude(self,saude):
        self.saude = saude
        self.alterarHumor()

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

    def alterarHumor(self):
        self.humor = (self.fome + self.saude)/2
    def mostrarHumor(self):
        return (self.fome + self.saude)/2

    def __str__(self):
        return f"""Nome: {self.nome}
Fome: {self.fome}
Saúde: {self.saude}
Idade: {self.idade}
Humor: {self.humor}"""

    def darComida(self,quantidade):
        self.fome -= quantidade
        self.alterarHumor()

    def brincar(self,tempo):
        self.humor += tempo



t = BichinhoVirtual('nome',15,15,20)
print(t)

t.alterarFome(30)

print(t)

n = 0
while n == 0:
    print('Opções do Menu')
    print('1 - Alterar Nome')
    print('2 - Alterar Fome')
    print('3 - Alterar Saúde')
    print('4 - Alterar Idade')
    print('5 - Dar Comida')
    print('6 - Brincar')

    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        nome = input('Digite o novo nome: ')
        t.alterarNome(nome)

    elif escolha == 2:
        fome = int(input('Digite Fome: '))
        t.alterarFome(fome)

    elif escolha == 3:
        saude = int(input('Digite a saúde: '))
        t.alterarSaude(saude)

    elif escolha == 4:
        idade = int(input('Digite a Idade? '))
        t.alterarIdade(idade)

    elif escolha == 5:
        quantidade = int(input('Dar quanto de Comida? '))
        t.darComida(quantidade)

    elif escolha == 6:
        tempo = int(input('Brincar por quanto tempo? '))
        t.brincar(tempo)
    else:
        print('Você escolheu uma opção secreta. Vejas os atributos do Bichinho Virtual!')
        print(t)