# Criação da lista
numeros = []

print("Digite 10 números:")
for i in range(10):
    while True:
        try:
            num = float(input(f"Elemento {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Por favor digite um número!")

print("\nLista original:", numeros)

# Ordenação por Bubble Sort
n = len(numeros)

for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Troca os elementos
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("\nLista ordenada (crescente):", numeros)