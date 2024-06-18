'''
Crie um classe chamada pessoa com os atributos: nome,
idade, peso, gênero
'''

class Pessoa():
    def __init__(self, nome: str, idade:int, peso:float, genero:str):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero
    
    def __str__(self) -> str:
        return f'O nome do paciente é {self.nome}, é do gênero {self.genero}, tem {self.idade} anos de idade, e pesa {self.peso} kg'


atributos_pessoa = Pessoa("Joana", 25, 64.5, "feminino")
print(atributos_pessoa)

atributos_pessoa2 = Pessoa("Luis", 30, 59, "masculino")
print(atributos_pessoa2)