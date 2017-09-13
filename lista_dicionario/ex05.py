a = 1
contatos = {}
while a:
    opcao = int(input("1 - Inserir\n2 - Remover\n3 - Pesquisar\n4 - Sair\nO que deseja fazer?\n"))
    if opcao == 1:
        nome = input("Qual o nome do contato?\n")
        email = input("Qual o e-mail do contato?\n")
        telefone = input("Qual o telefone do contato?\n")
        endereco = input("Qual o endereço do contato?\n")
        contatos[nome] = [email, telefone, endereco]
    elif opcao == 2:
        nome = input("Digite o nome do contato que deseja apagar:\n")
        del contatos[nome]
    elif opcao == 3:
        nome = input("Digite o nome do contato:\n")
        if nome in contatos:
            print(nome)
            j = 0
            for i in contatos[nome]:
                if j == 0:
                    print("E-mail: ", i)
                elif j == 1:
                    print("Telefone: ", i)
                elif j == 2:
                    print("Endereco: ", i)
                j += 1
        else:
            print("Contato nao encontrado.")
    elif opcao == 4:
        a = 0
    else:
        print("Opcao invalida.")