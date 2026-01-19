n = int(input("Tamanho da lista: "))
numeros = []

for i in range(n):
    while True:
        try:
            num = int(input(f"Elemento {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Digite um número inteiro!")

print("\nLista original:", numeros)

remover = int(input("Valor a remover (todas ocorrências): "))

numeros = [x for x in numeros if x != remover]

print("\nLista após remoção:", numeros)