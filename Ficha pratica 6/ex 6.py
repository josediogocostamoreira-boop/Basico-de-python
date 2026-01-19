contactos = []

while (True):
    print("\n\n***** Programa de Gestão de Contactos *****")
    print("1. Adicionar novo contacto")
    print("2. Atualizar contacto")
    print("3. Apagar contacto")
    print("4. Listar todos os contactos")
    print("0. Sair")

    opcao = int(input("Opção: "))

    if (opcao == 1):  # Adicionar novo contacto
        print("\nNOVO CONTACTO")

        novoNome = input("Nome: ")
        novoTelemovel = input("Telemovel: ")
        novoEmail = input("Email: ")
        novaCidade = input("Cidade: ")

        novoContacto = {
            "nome": novoNome,
            "telemovel": novoTelemovel,
            "email": novoEmail,
            "cidade": novaCidade
        }

        contactos.append(novoContacto)

    elif (opcao == 2):  # Atualizar contacto
        print("\nATUALIZAR CONTACTO")
        telemovelPesquisar = input("Telemóvel: ")

        for contactoAtual in contactos:
            if (contactoAtual["telemovel"] == telemovelPesquisar):
                # Encontramos o contacto que é para editar
                nomeEditado = input("Nome: ")
                emailEditado = input("Email: ")
                cidadeEditada = input("Cidade: ")

                contactoAtual["nome"] = nomeEditado
                contactoAtual["email"] = emailEditado
                contactoAtual["cidade"] = cidadeEditada

                print("CONTACTO EDITADO COM SUCESSO")

    elif (opcao == 3):  # Apagar contacto
        print("\nAPAGAR CONTACTO")
        telemovelPesquisar = input("Telemóvel: ")

        for contactoAtual in contactos:
            if (contactoAtual["telemovel"] == telemovelPesquisar):
                # Encontramos o contacto que é para apagar
                contactos.remove(contactoAtual)
                print("CONTACTO REMOVIDO COM SUCESSO")

    elif (opcao == 4):  # Listar todos os contactos
        for contactoAtual in contactos:
            print("____________________________")
            print(f"Nome: {contactoAtual["nome"]} | Telemovel: {contactoAtual["telemovel"]}")
            print(f"Email: {contactoAtual["email"]} | Cidade: {contactoAtual["cidade"]}")

    elif (opcao == 0):
        break
    else:
        print("Opção Inválida:", opcao)