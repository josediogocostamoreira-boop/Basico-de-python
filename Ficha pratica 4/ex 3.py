#numero inserido
numeroInserido = int(input("Insira um número para calcular os divisores: "))

#divisores
print("Divisores:")

#apresenta todos os divisores do numero inserido
for i in range(1, numeroInserido + 1):
    if (numeroInserido % i == 0):
        print(i)
