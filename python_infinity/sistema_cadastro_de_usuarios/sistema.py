'''
Faça um sistema em python para realizar o cadastro de usuários. 
Cada usuário deve ter nome, e-mail e idade.
Deve ser possível adicionar, remover e listar os usuário.
'''

#importando a biblioteca time para poder dar um tempo de espera no menu 
import time

#criação da lista onde serão armazenados os usuários
lista_usuarios = []

# Função para adicionar usuários
def adicionar_usuario(nome,email,idade):
    dict_usuario = {
        "Nome":nome,
        "E-mail":email,
        "Idade":idade}
    
    #adicionando o usuário à lista de usuários
    lista_usuarios.append(dict_usuario)
    
    print("Usuário cadastrado com sucesso!")

#Função para listar os usuários
def listar_usuarios():
    #verificando se a lista está vazia
    if len(lista_usuarios) == 0:
       print("Nenhum usuário foi encontrado no nosso sistema.") 
    else:
        #percorrendo a lista de usuários e exibindo cada usuário
        for usuario in lista_usuarios:
            print(f"Nome: {usuario['Nome']}, E-mail: {usuario['E-mail']}, Idade: {usuario['Idade']}.")


#Função para remover algum usuário pelo nome
def remover_usuario(nome):
    #percorrendo a lista de usuários
    for usuario in lista_usuarios:
        #se o usuário informado tiver um valor igual ao do usuário cadastrado, irei removê-lo
        if usuario['Nome'] == nome:
            lista_usuarios.remove(usuario)
            print("Usuário removido com sucesso!")

#Função para criação do menu para o usuário 
def menu():
    while True:
        print('''
            #### Boas vindas ao nosso sistema de cadastro de usuários! ####\n
            Escolha qual opção você deseja realizar:\n
            1 - Adicionar novo usuário\n
            2 - Listar todos os usuários\n
            3 - Remover um usuário\n
            0 - Sair do Sistema\n
        ''')

        opcao_usuario = input("Digite a opção desejada: ")

        match opcao_usuario:
            case '0':
                print("SAINDO DO SISTEMA...")
                break

            case '1':
                nome_usuario = input("Digite o nome do usuário: ").title() #O .title() transforma a primeira letra de cada string em maiúsculo
                email_usuario = input("Digite o e-mail do usuário: ")

                #laço de repetição while True para verificar se o usuário está informando o e-mail com as informações devidas. caso não esteja, é feita uma verificação do que está faltando e pede apenas o e-mail do usuário novamente
                while True:
                    if '@' not in email_usuario:
                        print("E-mail inválido! O e-mail informado deve conter @")
                    elif '.com' not in email_usuario:
                        print("E-mail inválido! O e-mail informado deve conter .com")
                    else:
                        break
                    email_usuario = input("Digite o e-mail do usuário: ")

                idade_usuario = int(input("Digite a idade do usuário: "))

                #loop while para verificar se a idade do usuário é válida(não é permitida a inserção de idades com valores negativos). caso o usuário informe uma idade que contenha este tipo de invalidez, a idade será pedida novamente até que seja fornecida a informação correta
                while idade_usuario < 0:
                    print("Idade inválida! Informe sua idade novamente.")
                    idade_usuario = int(input("Digite a idade do usuário: "))

                adicionar_usuario(nome_usuario, email_usuario, idade_usuario)

                time.sleep(1.5) #tempo de espera de 1.5 segundos até aparecer o menu novamente

            case '2':
                listar_usuarios()
                time.sleep(1.5)

            case '3':
                #verificando se a lista de usuários está vazia. se estiver, exibe a mensagem de aviso e volta para o menu
                if len(lista_usuarios) == 0:
                    print("Nenhum usuário foi encontrado no nosso sistema.")
                    time.sleep(1.5)
                    continue

                usuario_a_ser_removido = input("Digite o nome do usuário a ser removido: ").capitalize()
                remover_usuario(usuario_a_ser_removido)

                time.sleep(1.5)

#Chamando a função do menu
menu()