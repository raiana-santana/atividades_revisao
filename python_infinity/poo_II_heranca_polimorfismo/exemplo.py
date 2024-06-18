class Animal:

    def __init__(self, especie, nome, idade, peso):
        self.especie = especie
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        return "Au au"
    
    def __repr__(self):
        return f"{self.especie}\n {self.nome}, {self.idade} ano(s), {self.peso} kg, Som: {self.fazer_som()}"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau miau"
    
    def __repr__(self):
        return f"{self.especie}\n {self.nome}, {self.idade} ano(s), {self.peso} kg, Som: {self.fazer_som()}"
    

class Galinha(Animal):
    def fazer_som(self):
        return "Cocórico"
    
    def __repr__(self):
        return f"{self.especie}:\n{self.nome}, {self.idade} ano(s), {self.peso} kg, Som: {self.fazer_som()}"
    

cachorro = Cachorro("CACHORRO", "Rex", 4, 4.5)
print(cachorro)

gato = Gato("GATO", "Mia", 2, 2.6)
print(gato)

galinha = Galinha("GALINHA", "Gertrudes", 1, 1.5)
print(galinha)