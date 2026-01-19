# Criar lista vazia
numeros = []

# Preencher a lista com 10 valores
print("Digite 10 números:")
for i in range(10):
    num = int(input(f"Elemento {i+1}: "))
    numeros.append(num)

# Mostrar a lista
print("\nLista completa:", numeros)

# Pesquisar um valor
procurar = int(input("\nQual número deseja procurar na lista? "))

# Verificar se existe
if procurar in numeros:
    print(f"O número {procurar} ESTÁ na lista!")
else:
    print(f"O número {procurar} NÃO está na lista.")