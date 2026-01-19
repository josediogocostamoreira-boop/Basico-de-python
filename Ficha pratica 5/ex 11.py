# Pergunta o tamanho da lista
while True:
    try:
        tamanho = int(input("Qual o tamanho da lista que deseja criar? "))
        if tamanho > 0:
            break
        else:
            print("O tamanho deve ser um número positivo!")
    except ValueError:
        print("Por favor, digite um número inteiro!")

# Criar a lista vazia
lista = []

# Preencher a lista
print(f"\nAgora digite {tamanho} valores:")
for i in range(tamanho):
    while True:
        try:
            valor = input(f"Elemento {i + 1}: ")
            # Tenta converter para número, mas aceita qualquer coisa como string
            try:
                valor = float(valor)  # tenta número real
            except ValueError:
                pass  # mantém como string se não for número

            lista.append(valor)
            break
        except:
            print("Erro ao ler o valor. Tente novamente.")

# Mostrar a lista na ordem de inserção
print("\n" + "=" * 50)
print("Lista na ordem de inserção:")
print("=" * 50)

for i, elemento in enumerate(lista, 1):
    print(f"Posição {i}: {elemento}")