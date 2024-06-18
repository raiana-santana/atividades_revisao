class Pessoa:
    def __init__(self, nome, sobrenome, cpf) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
    def identificacao(self):
        return self.cpf
    

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, codigo) -> None:
        super().__init__(nome, sobrenome, cpf)
        self.codigo = codigo

    def identificacao(self):
        return self.codigo


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula) -> None:
        super().__init__(nome, sobrenome, cpf)
        self.matricula = matricula

    def identificacao(self):
        return self.matricula

cliente1 = Cliente("Raiana", "Santana", "084.286.875-52", "001")
funcionario1 = Funcionario("Joana", "Silva", "000.258.451-59", "123")

print(cliente1.nome_completo())
print(cliente1.identificacao())
print("#######################")
print(funcionario1.nome_completo())
print(funcionario1.identificacao())
