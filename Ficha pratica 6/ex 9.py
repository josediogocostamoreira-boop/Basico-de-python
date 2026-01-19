vendas = {}

while True:
    print("programa de gestão de vendas: ")
    print("1 - Registar venda")
    print("2 - Ver total de um produto")
    print("3 - Mostrar todas as vendas")
    print("4 - Sair")

    opção = int(input("Opção: "))

    if opção == 1:
        print("Registar venda")
        produto = input("Nome do produto: ")

        if produto in vendas:
            quantidade = int(input("Quantidade: "))
            vendas[produto][0] += quantidade
        else:
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            vendas[produto] = [quantidade, preco]

    elif opção == 2:
        print("\nTotal de vendas do produto")
        produto = input("Nome do produto: ")

        if produto in vendas:
            qtd = vendas[produto][0]
            preco = vendas[produto][1]
            total = qtd * preco
            print("Produto:", produto)
            print("Quantidade vendida:", qtd)
            print("Preço:", preco)
            print("Total:", total)
        else:
            print("Produto não encontrado")

    elif opção == 3:
        print("\nLista de vendas")
        print(vendas)

    elif opção == 4:
        print("\nA sair...")
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








