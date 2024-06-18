'''
construir um carro. o carro tem os atributos: cor, ano, marca
vamos adicionar o self.velocidade para poder acelerar e frear o carro
'''

class Carro:
    def __init__(self, cor, ano, marca):
        self.cor = cor
        self.ano = ano
        self.marca = marca
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 10
        return f'O carro de cor {self.cor}, do ano {self.ano} e marca {self.marca} está acelerando a {self.velocidade}'
    
    def frear(self):
        self.velocidade -= 5
        return f'O carro agora freou e está a uma velocidade de {self.velocidade}'
    
#primeiro vamos construir o carro 
carro1 = Carro("vermelho", 2001, "fiat")

#vamos agora partir para as abstrações de velocidade
print(carro1.acelerar())
print(carro1.frear())