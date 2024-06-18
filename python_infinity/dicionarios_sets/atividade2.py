'''Escreva um programa que percorra um dicionário 
contendo informações de pessoas (nome, idade) e exiba essas informações.'''

pessoas = [
    {"nome": "Ana", "idade": 60},
    {"nome": "Raiana", "idade": 24},
    {"nome": "Andressa", "idade": 24}
]

for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")


# for i in range(len(pessoas)):
#     print(f"Nome: {pessoas[i]['nome']}, Idade: {pessoas[i]['idade']}")