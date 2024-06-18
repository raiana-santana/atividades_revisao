# Crie uma classe Empresa que permita gerenciar
# funcionários. Os funcionários devem ter informações
# como nome, cargo e salário. A empresa deve ser capaz
# de adicionar, remover e listar funcionários.

class Empresa():
    def __init__(self):
        self.funcionarios = []

    def remover(self, nome):
        for funcionario in self.funcionarios:
            if funcionario["nome"] == nome:
                self.funcionarios.remove(funcionario)

    def adicionar(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar(self):
        return self.funcionarios
    

funcionario = {
    "nome":"Maria",
    "cargo":"Motorista",
    "salario": 2300
}

funcionario2 = {
    "nome":"João",
    "cargo":"Jardineiro",
    "salario": 1000
}

funcionario3 = {
    "nome":"José",
    "cargo":"Zelador",
    "salario": 1500
}

empresa = Empresa()

empresa.adicionar(funcionario)
empresa.adicionar(funcionario2)
empresa.adicionar(funcionario3)

print(empresa.listar())

funcionario_para_remover = input("Informe o nome do funcionário que deseja remover: ")
empresa.remover(funcionario_para_remover)
print(empresa.listar())
