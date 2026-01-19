# Criar uma lista vazia
lista = []

# Pedir 10 números e guardar na lista
i = 1
while i <= 10:
    num = int(input("Insira o número " + str(i) + "/10: "))
    lista.append(num)
    i = i + 1

# Mostrar a lista na ordem normal
print("Lista na ordem de inserção:")
print(lista)

# Mostrar a lista na ordem inversa
print("Lista na ordem inversa:")
j = 9
while j >= 0:
    print(lista[j])
    j = j - 1