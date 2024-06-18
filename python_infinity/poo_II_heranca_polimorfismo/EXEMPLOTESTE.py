'''
criar uma classe pessoa que recebe atributos de nome e idade
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def __repr__(self) -> str:
        return f'Olá {self.nome}, você tem {self.idade} anos'
    
atributos_pessoa = Pessoa("Raiana", 24)
print(atributos_pessoa)

'''
exemplo de herança e polimorfismo
classe animal e as subclasses cachorro, gato, galinha
'''

class Animal:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return 'Au au'
    
    def __repr__(self) -> str:
        return f'Seu bichinho se chama {self.nome}, tem {self.idade} anos e pesa {self.peso} quilos. O som que ele faz é {self.fazer_som()}'
    
doguinho = Cachorro("Rex", 2, 1.5)
print(doguinho)

##########################################
class Veiculo:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def __repr__(self) -> str:
        return f'Modelo: {self.modelo}. Cor: {self.cor}'
    
class Bicicleta(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo, cor)

class Carro(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo, cor)

bicicletinha = Bicicleta("Mountain Bike", "Rosa")
carrinho = Carro("Fusca", "Azul")

print(bicicletinha)
print(carrinho)