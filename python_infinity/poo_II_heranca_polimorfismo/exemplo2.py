#criar classes pessoa, onde recebe, nome, sobrenome, cpf, tenho o metodo nome completo e idenficacao
#classe cliente, que herda de pessoa, mas tem um codigo como identificacao
#classe funcionario, que herda tbm de pessoa, mas tem uma matricula como identificacao 

# abstração, herança, polimorfismo

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
    def identificacao(self):
        return self.cpf

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, codigo):
        super().__init__(nome, sobrenome, cpf)
        self.codigo = codigo

    def identificacao(self):
        return self.codigo
    
class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.matricula = matricula

    def identificacao(self):
        return self.matricula
    
cliente1 = Cliente("Raiana", "Santana", "123.456.789-11", "0123")
print(cliente1.nome_completo())
print(cliente1.identificacao())
print("###########################################")
funcionario1 = Funcionario("Jose", "Freitas", "321.654.987-12", "1236")
print(funcionario1.nome_completo())
print(funcionario1.identificacao())


# pessoa = Pessoa("Rai", "Barril", "444478448")
# print(pessoa.nome_completo())
# print(pessoa.identificacao())