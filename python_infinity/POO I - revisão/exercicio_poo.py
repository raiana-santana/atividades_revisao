# Crie um classe chamada cachorro com os atributos:
# nome, raça, idade


class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome} ; Raça: {self.raca} ; Idade: {self.idade} anos de idade"

cachorro1 = Cachorro("max", "pitbull", 2)
print(cachorro1)