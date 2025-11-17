opcao=0

while True:
    # Mostrar o menu
    print("\nMenu:")
    print("1. Criar")
    print("2. Atualizar")
    print("3. Eliminar")
    print("4. Sair")

    # Ler a opção do utilizador
    opcao = input("Escolha uma opção (1-4): ")

    # Verificar a opção escolhida
    if opcao == '1':
        print("Opção escolhida: Criar")
    elif opcao == '2':
        print("Opção escolhida: Atualizar")
    elif opcao == '3':
        print("Opção escolhida: Eliminar")
    elif opcao == '4':
        print("A sair do programa... Até à próxima!")

    else:
        print("Opção inválida! Por favor, escolha entre 1 e 4.")