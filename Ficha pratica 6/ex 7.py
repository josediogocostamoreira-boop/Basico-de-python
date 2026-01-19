livros = []

while True:
    print("programa de gestão de livros: ")
    print("1 - Novo Livro")
    print("2 - Alterar Disponibilidade por ISBN")
    print("3 - Mostrar todos os livros")
    print("4 - Remover livro por ISBN")
    print("5 - Sair")

    opção = int(input("Opção: "))

    if opção == 1: #adicionar livro
        print("Novo Livro")
        novoISBN = input("ISBN: ")
        novoTitulo = input("Titulo: ")
        novoAutor = input("Autor: ")
        novoAnoPublicação = input("Ano de publicação: ")
        novoDisponibilidade = input("Disponibilidade (true ou false): ")

        novoLivro = {
            "ISBN": novoISBN,
            "Titulo": novoTitulo,
            "Autor": novoAutor,
            "Ano de publicação": novoAnoPublicação,
            "Disponibilidade": novoDisponibilidade
        }

        livros.append(novoLivro)

    elif (opção == 2):  # atualizar disponibilidade
        print("\nAtualizar Disponibilidade")
        ISBNpesquisar = input("ISBN: ")

        for livroAtual in livros:
            if (livroAtual["ISBN"] == ISBNpesquisar):
                # Encontramos o livro
                DisponibilidadeEditada = input("disponibilidade: ")

                livroAtual["Disponibilidade"] = DisponibilidadeEditada

            if (livroAtual["ISBN"] != ISBNpesquisar):
                print("livro não encontrado")


    elif (opção == 3): #listar todos os livros
        print("\nLista de livros")
        print(livros)




    elif (opção == 4):  # Remover livro
        print("\nRemover Livro")
        ISBNpesquisar = input("ISBN: ")

        for livroAtual in livros:
            if (livroAtual["ISBN"] == ISBNpesquisar):
                # Encontramos o livro que é para apagar
                livros.remove(livroAtual)
                print("LIVRO REMOVIDO COM SUCESSO")



    elif (opção == 5): #fechar
        print("\nShuting Down")
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
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠒⠒⢲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
