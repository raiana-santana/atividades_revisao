#HERANÇA

class Animal:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        pass



class Cachorro(Animal):
    def fazer_som(self):
        return "Au au"
    
    def __repr__(self):
        return f"{self.nome}, {self.idade} anos - Som: {self.fazer_som()}"



class Gato(Animal):
    def fazer_som(self):
        return "Miau"
    
    def __repr__(self):
        return f"{self.nome}, {self.idade} anos - Som: {self.fazer_som()}"
    

cachorro = Cachorro("Rex", 2)
gato = Gato("Mia", 3)

print(cachorro)
print(gato)