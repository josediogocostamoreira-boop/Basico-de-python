dicionarioCompras = {
    "Água 1L": 1.5,
    "Batatas": 2.9,
    "Vinho": 10.0
}

while (True):
    print("\n\n**** Programa Lista de Compras *****")
    print("1. Consultar Lista")
    print("2. Adicionar Produto")
    print("3. Calcular Total")
    print("0. Sair")

    opcao = int(input("Opção: "))

    if (opcao == 1):  # Consultar Lista
        print(dicionarioCompras)

    elif (opcao == 2):  # Adicionar Produto
        novoProduto = input("Novo Produto: ")
        novoPreco = float(input("Preço: "))

        dicionarioCompras[novoProduto] = novoPreco
        print("Produto novo adicionado com sucesso")

    elif (opcao == 3):  # Calcular Total
        listaPrecos = dicionarioCompras.values()
        totalLista = sum(listaPrecos)
        print("Total:", totalLista, "€")

    elif (opcao == 0):  # Sair
        break

    else:
        print("Opção Inválida:", opcao)