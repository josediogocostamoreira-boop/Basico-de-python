# 1. Criação e preenchimento da lista
lista = []

print("Digite 10 números inteiros:\n")
for i in range(10):
    while True:
        try:
            numero = int(input(f"Elemento {i+1}: "))
            lista.append(numero)
            break
        except ValueError:
            print("Por favor, digite apenas números inteiros!\n")

# 2. Mostrar a lista preenchida
print("\nLista completa:", lista)

# 3. Pedir o valor a pesquisar
while True:
    try:
        valor = int(input("\nQual valor deseja procurar na lista? "))
        break
    except ValueError:
        print("Digite um número inteiro válido!\n")

# 4. Procurar todas as posições onde o valor aparece
posicoes = []
for i in range(len(lista)):
    if lista[i] == valor:
        posicoes.append(i)

# 5. Mostrar resultado
if posicoes:
    print(f"\nO valor {valor} foi encontrado nas seguintes posições:")
    for pos in posicoes:
        print(f"→ índice {pos}  (posição {pos+1})")
    print(f"\nTotal de ocorrências: {len(posicoes)}")
else:
    print(f"\nO valor {valor} NÃO foi encontrado na lista.")