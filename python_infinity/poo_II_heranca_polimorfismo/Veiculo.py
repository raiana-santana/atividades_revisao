class Veiculo:
    def __init__(self, modelo, cor):
        # self.tipo = tipo
        self.modelo = modelo
        self.cor = cor

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}:\n Modelo -> {self.modelo},\n Cor -> {self.cor}"
    

class Carro(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo, cor)

class Bicicleta(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo, cor)

carro = Carro("Sedan", "Vermelho")
print(carro)

bicicleta = Bicicleta("Mountain Bike", "Rosa")
print(bicicleta)