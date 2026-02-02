# Programa de presenças

funcionarios = {
    1234: "Joaquim Alberto",
    2233: "Fernando Mendes",
    4343: "Joana Lima",
    5678: "Ana Silva"
}

presencas = {
    1234: ["03-12-2024", "04-12-2024"],
    2233: ["02-12-2024", "03-12-2024", "05-12-2024"],
    4343: ["04-12-2024"],
    5678: ["03-12-2024", "04-12-2024", "05-12-2024"]
}

# Dados do administrador
ADMIN_ID = 119999
ADMIN_PASSWORD = "admin123"   # <--- podes mudar esta password

opcao = 1

while opcao != 0:
    print("\n--- SISTEMA DE PRESENÇAS ---")
    print("Escreve o teu número de funcionário")
    print("(ou 119999 para tentar entrar como administrador)")
    print("0 para sair")

    numero = input("Número: ")

    if numero == "0":
        opcao = 0
        continue

    # Converter para número
    try:
        id = int(numero)
    except:
        print("Escreve só números!")
        continue

    # =====================================
    #   FUNCIONÁRIO NORMAL
    # =====================================
    if id != ADMIN_ID:

        if id not in funcionarios:
            print("Número não existe!")
            continue

        nome = funcionarios[id]

        opcao_func = 1
        while opcao_func != 0:

            print("\nOlá", nome)
            print("1 → Registar presença")
            print("2 → Ver as minhas presenças")
            print("0 → Voltar atrás")

            opcao_func = input("Escolhe: ")

            if opcao_func == "1":
                dia = input("Dia (ex: 05): ")
                mes = input("Mês (ex: 12): ")
                ano = input("Ano (ex: 2024): ")

                data = dia + "-" + mes + "-" + ano

                if id not in presencas:
                    presencas[id] = []

                if data in presencas[id]:
                    print("Já tinhas marcado este dia!")
                else:
                    presencas[id].append(data)
                    print("Presença guardada →", data)

            elif opcao_func == "2":
                if id not in presencas or len(presencas[id]) == 0:
                    print("Ainda não tens presenças.")
                else:
                    print("\nAs tuas presenças:")
                    for d in presencas[id]:
                        print("  •", d)
                    print("Total:", len(presencas[id]), "dias")

            elif opcao_func == "0":
                break

            else:
                print("Opção errada!")

    # =====================================
    #  ADMINISTRADOR
    # =====================================
    else:

        print("\n--- MODO ADMINISTRADOR ---")
        password = input("Password: ")

        if password != ADMIN_PASSWORD:
            print("Password errada! Não podes entrar.")
            continue

        # Se a password estiver correta → entra no menu admin
        print("Bem-vindo, Administrador!")

        opcao_admin = 1
        while opcao_admin != 0:

            print("\n--- MENU ADMINISTRADOR ---")
            print("1 → Adicionar funcionário novo")
            print("2 → Ver quem tem mais presenças")
            print("0 → Voltar atrás")

            opcao_admin = input("Escolhe: ")

            if opcao_admin == "1":
                novo_numero = input("Número novo: ")
                try:
                    novo_id = int(novo_numero)
                except:
                    print("Número inválido!")
                    continue

                if novo_id in funcionarios:
                    print("Este número já existe!")
                    continue

                nome_novo = input("Nome do funcionário: ")
                if nome_novo == "":
                    print("Tem de colocar um nome!")
                    continue

                funcionarios[novo_id] = nome_novo
                presencas[novo_id] = []
                print("Funcionário adicionado!")

            elif opcao_admin == "2":
                if len(presencas) == 0:
                    print("Ninguém tem presenças ainda.")
                    continue

                maior = 0
                quem = ""

                for id_func, lista in presencas.items():
                    if len(lista) > maior:
                        maior = len(lista)
                        quem = funcionarios[id_func]

                print("\nQuem tem mais presenças:")
                print(quem, "→", maior, "dias")

            elif opcao_admin == "0":
                break

            else:
                print("Opção errada!")

print("\nObrigado! Até à próxima!")

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