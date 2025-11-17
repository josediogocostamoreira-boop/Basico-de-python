# Ler número do utilizador
numero = int(input("Introduza um número: "))

# Verificar se é primo
if numero <= 1:
    print(f"{numero} não é um número primo.")
else:
    primo = True  # assumimos que é primo até provar o contrário

    for i in range(2, numero):
        if numero % i == 0:
            primo = False


    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")