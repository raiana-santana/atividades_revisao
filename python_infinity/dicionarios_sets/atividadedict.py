'''
Escreva um programa que recebe um dicionário e uma
lista de chaves como entrada e verifica se todas as
chaves da lista existem no dicionário. A função deve
retornar True se todas as chaves existirem e False caso
contrário.

dicionario = {'nome': 'raiana', 'idade':24, 'genero': 'feminino'}
lista_de_chaves = ['nome', 'idade', 'genero']

todas_as_chaves_existem = True 

for chave in lista_de_chaves:
    if chave not in dicionario:
        todas_as_chaves_existem = False
        break

print(todas_as_chaves_existem)
'''

#########################################################################################################

'''
Desenvolva um programa que recebe um dicionário, uma
chave e um valor como entrada e adiciona a chave e o
valor ao dicionário, atualizando o valor se a chave já
existir.
'''

dicionario = {}

numero_de_pares_chave_valor = int(input("Quanto pares chave-valor você quer adicionar no dicionário? "))

for i in range(numero_de_pares_chave_valor):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")

    if chave not in dicionario:
        print(f"Atualizando o valor da chave {chave} para {valor}")
    else:
        print(f"Adicionando a chave {chave} com o valor {valor}")

    dicionario[chave] = valor 

print(f"\nDicionário atualizado:\n{dicionario}")