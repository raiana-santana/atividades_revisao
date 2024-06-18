'''
Crie uma hierarquia de classes que represente veículos.
Comece com uma classe base "Veículo" e, em seguida,
crie classes derivadas como "Carro" e "Bicicleta." 
Adicione métodos para definir atributos, como "cor"
e "modelo" e permita a chamada de métodos em cadeia para configurar esses atributos.
'''

class Veiculo:
    def __init__(self, tipo, modelo, cor):
        self.tipo = tipo
        self.modelo = modelo
        self.cor = cor

    def __repr__(self) -> str:
        return f"{self.tipo}: Modelo: {self.modelo}, Cor: {self.cor}"


class Carro(Veiculo):
    def __init__(self, tipo, modelo, cor):
        super().__init__(tipo, modelo, cor)


class Bicicleta(Veiculo):
    def __init__(self, tipo, modelo, cor):
        super().__init__(tipo, modelo, cor)



carro = Carro("Carro", "Sedan", "Vermelho")
print(carro)  

bicicleta = Bicicleta("Bicicleta", "Mountain Bike", "Rosa")
print(bicicleta)  
