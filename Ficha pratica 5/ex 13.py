# 1. Perguntar o tamanho da lista
while True:
    try:
        tamanho = int(input("Qual o tamanho da lista? "))
        if tamanho > 0:
            break
        print("O tamanho deve ser maior que zero!")
    except ValueError:
        print("Por favor, digite um número inteiro!")

# 2. Criar e preencher a lista
lista = []

print(f"\nDigite {tamanho} valores:")
for i in range(tamanho):
    while True:
        try:
            valor = input(f"Elemento {i + 1}: ")
            # Tenta converter para número (se falhar, mantém como string)
            try:
                valor = float(valor)
            except ValueError:
                pass
            lista.append(valor)
            break
        except:
            print("Erro ao ler. Tente novamente.")

# 3. Mostrar lista atual
print("\nLista atual:", lista)

# 4. Perguntar o novo valor e a posição
while True:
    try:
        novo_valor = input("\nQual valor deseja inserir? ")
        # Tenta converter para número (consistência com a lista)
        try:
            novo_valor = float(novo_valor)
        except ValueError:
            pass

        posicao = int(input(f"Em que posição (0 a {len(lista)})? "))

        if 0 <= posicao <= len(lista):
            break
        else:
            print(f"A posição deve estar entre 0 e {len(lista)}!")

    except ValueError:
        print("Digite valores válidos!")

# 5. Inserir o elemento na posição desejada
lista.insert(posicao, novo_valor)

# 6. Mostrar resultado final
print("\n" + "-" * 50)
print("Lista após inserção:")
print("-" * 50)
print(lista)
print(f"Tamanho final: {len(lista)} elementos")