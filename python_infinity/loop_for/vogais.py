# palavra_usuario = input("Digite uma palavra para poder remover as vogais: ")
# palavra_sem_vogais = ''
# vogais = 'aAeEiIoOuU'

# for letra in palavra_usuario:
#     if letra not in vogais:
#         palavra_sem_vogais += letra

# print(palavra_sem_vogais)


# word_user = input("Digite uma palavra para podermos contar quantas consoantes essa palavra tem: ")
# vowels = "aAeEiIoOuU"
# counter = 0

# for letra in word_user:
#     if letra not in vowels:
#         counter += 1

# print(f"Essa palavra tem {counter} consoantes")

# soma = 0

# while True:
#     numero_usuario = int(input("Digite um número para somar (0 para sair): "))

#     if numero_usuario == 0:
#         print(soma)
#         break
#     else:
#         soma += numero_usuario

while True:
    print("#### Seja bem vindo à Calculadora ####")
    print("Digite + para fazer uma conta de adição")
    print("Digite - para fazer uma conta de subtração")
    print("Digite * para fazer uma conta de multiplicação")
    print("Digite / para fazer uma conta de divisão")
    print("Digite 0 para sair")


    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Saindo do sistema...")
        break
    elif opcao == '+':
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        soma = numero1 + numero2
        print(f"O resultado da soma entre {numero1} e {numero2} é igual a {soma}")
    elif opcao == '-':
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        sub = numero1 - numero2
        print(f"O resultado da soma entre {numero1} e {numero2} é igual a {sub}")
    elif opcao == '*':
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        mult = numero1 * numero2
        print(f"O resultado da soma entre {numero1} e {numero2} é igual a {mult}")
    elif opcao == '/':
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        div = numero1 / numero2
        print(f"O resultado da soma entre {numero1} e {numero2} é igual a {div}")
    else:
        print("Opção inválida, tente novamente.")