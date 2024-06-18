#POLIMORFISMO

class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def area(self):
        return self.altura * self.base
    
    def __repr__(self) -> str:
        return f"A área do retângulo que possui base de altura de {self.altura} e {self.base} tem uma área de {self.area()}"
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio**2
    
    def __repr__(self) -> str:
        return f"O círculo que possui um raio de {self.raio} tem uma área de {self.area()}"
    

def imprimir_area(forma):
    print(forma)

retangulo = Retangulo(8, 2)
circulo = Circulo(5)

imprimir_area(retangulo)
imprimir_area(circulo)