class Animal:
    def emitirSom(self):
        pass

class Cachorro(Animal):
    def emitirSom(self):
        return "Au au"

class Gato(Animal):
    def emitirSom(self):
        return "Miau"
    
class Passaro(Animal):
    def emitirSom(self):
        return "Piu"
    

cachorro = Cachorro()
gato = Gato()
passaro = Passaro()

animais = [cachorro, gato, passaro]

for animal in animais:
    print(animal.emitirSom())