class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio**2
    
    def __repr__(self) -> str:
        return f"A área do círculo que tem raio de {self.raio} é de {self.area()}"
    
class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def __repr__(self) -> str:
        return f"A área do retângulo que tem base {self.base} e altura de {self.altura} é de {self.area()}"
    

circulo = Circulo(5)
print(circulo)

retangulo = Retangulo(2, 2)
print(retangulo)