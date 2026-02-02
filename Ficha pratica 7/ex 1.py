ranking = []

while True:
    print("Programa de Gestão de Ranking de Esports")
    print("ranking:", ranking)
    print("\n1 - Novo Jogador")
    print("2 - Atualizar Pontuação por Nome")
    print("3 - Mostrar todos os jogadores")
    print("4 - Mostrar jogador com maior pontuação")
    print("5 - Sair")

    opção = int(input("Opção: "))

    if opção == 1:  # adicionar jogador
        print("\nNovo Jogador")
        nome = input("Nome: ")
        pontuacao = input("Pontuação inicial: ")

        novoJogador = {
            "nome": nome,
            "pontuacao": pontuacao
        }

        ranking.append(novoJogador)

    elif opção == 2:  # atualizar pontuação
        print("\nAtualizar Pontuação")
        nome_pesquisar = input("Nome do jogador: ")

        encontrado = False
        for jogador in ranking:
            if jogador["nome"] == nome_pesquisar:
                nova_pontuacao = input("Nova pontuação: ")
                jogador["pontuacao"] = nova_pontuacao
                encontrado = True
                print("Pontuação atualizada!")
                break

        if not encontrado:
            print("Jogador não encontrado")

    elif opção == 3:  # listar todos
        print("\nLista de Jogadores")
        if len(ranking) == 0:
            print("Ainda não existem jogadores registados")
        else:
            for jogador in ranking:
                print(jogador)

    elif opção == 4:  # mostrar o melhor
        print("\nJogador com maior pontuação")

        if len(ranking) == 0:
            print("Ainda não existem jogadores registados")
        else:
            melhor = ranking[0]
            for jogador in ranking:
                if int(jogador["pontuacao"]) > int(melhor["pontuacao"]):
                    melhor = jogador

            print("Melhor jogador:")
            print(melhor)

    elif opção == 5:
        print("\nA sair do programa...")
        break

    else:
        print("Opção Inválida:", opção)

#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣠⣴⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀ ⢀⣴⣾⠟⢹⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀  ⣠⣶⡿⠋⠁⠀⢸⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⡿⠿⠛⠛⠋⠉⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀
# ⢀⣴⡿⠟⠁⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀
#⠐⠿⣿⣤⡀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄
#⠀⠀⠀⣿⣿⣷⣄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⣿⣇⣀⣠⠴⠶⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⣿⣿⣿⡿⠇
#⠀⠀⠀⣿⣿⣿⣿⣿⣦⡀⢸⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠛⠛⠛⠛⠛⠛⠿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠒⠒⢲⠀