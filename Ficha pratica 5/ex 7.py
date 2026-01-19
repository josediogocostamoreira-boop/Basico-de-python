# Criar uma lista vazia
lista = []

# Variável para guardar o maior par (começa com um valor muito pequeno)
maior_par = -999999

# Variável para saber se encontrou pelo menos um par
encontrou_par = 0  # 0 = não, 1 = sim

# Pedir 10 números ao utilizador
i = 1
while i <= 10:
    num = int(input("Insira o número " + str(i) + ": "))
    lista.append(num)

    # Se o número for par
    if num % 2 == 0:
        encontrou_par = 1
        if num > maior_par:
            maior_par = num
    i = i + 1

# Mostrar a lista
print("Os números inseridos foram:", lista)

# Mostrar o resultado
if encontrou_par == 1:
    print("O maior valor par inserido foi:", maior_par)
else:
    print("Não foi inserido nenhum número par.")


