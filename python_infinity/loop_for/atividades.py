#se inicia em 0, vai até 15, e vai de dois em dois
# for num in range (0, 15, 2):
#     print(num)

#########################################################
#a soma dos números de 1 a 100
# soma = 0

# for num in range (1, 101):
#     soma+=num

# print(f"A soma dos número de 1 a 100 é {soma}")
#########################################################
'''
1. Crie um programa que imprima os números pares de 2 a 10.
'''
# for num in range (2, 11, 2):
#     print(num)
#########################################################
'''
2. Utilize um loop for para calcular o produto dos números de 1
a 5.
'''
# mult = 1

# for num in range(1, 6):
#     mult*=num

# print(f"O produto dos números de 1 a 5 é igual a {mult}")
#########################################################
'''
Utilize um loop for para imprimir os números de 1 a 20,
pulando os múltiplos de 3.
'''
# for i in range(1, 21):
#     if i % 3 == 0:
#         print(i)
#########################################################
'''
Crie uma programa que solicite 10 números para o usuário.
O programa deve somar todos os números múltiplos de 6
digitados. Se a soma for igual ou maior que 30, o programa
dever parar e mostrar o resultado da soma.
'''
# soma = 0

# for num in range(10):
#     numero = int(input("Digite um número: "))

#     if numero % 6 == 0:
#         soma+=numero
#     elif soma>=30:
#         break

# print(f"Soma dos números múltiplos de 6: {soma}")


senha = input("Digite sua senha: ")
tentativas = 3

for i in range (3):
    usuario = input("confira a senha: ")

    if usuario == senha:
        print("bem vindo!")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta você tem mais {tentativas} tentativas")
        if tentativas == 0:
            print("Você atingiu o limite de tentativas. Telefone bloqueado")
            break