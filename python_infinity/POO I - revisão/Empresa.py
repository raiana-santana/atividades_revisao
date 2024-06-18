class Empresa:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.funcionarios = []

    def listar(self):
        return self.funcionarios
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, nome):
        for funcionario in self.funcionarios:
            funcionario["nome"]==nome
            self.funcionarios.remove(funcionario)