# Programa que separa números pares e ímpares

# 1. Criar e preencher a lista com 15 números
numeros = []

print("Digite 15 números inteiros:\n")
for i in range(15):
    while True:
        try:
            num = int(input(f"Número {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Por favor, digite apenas números inteiros!")

# 2. Mostrar a lista original
print("\nLista original:", numeros)

# 3. Criar as duas novas listas
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:      # resto da divisão por 2 é zero → par
        pares.append(numero)
    else:
        impares.append(numero)

# 4. Mostrar os resultados
print("\n" + "-" * 60)
print("Números PARES:", pares)
print("Quantidade de pares:", len(pares))
print("-" * 60)
print("Números ÍMPARES:", impares)
print("Quantidade de ímpares:", len(impares))
print("-" * 60)