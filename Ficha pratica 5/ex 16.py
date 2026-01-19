# Programa que encontra os elementos comuns entre duas listas

# 1. Preencher a primeira lista
lista1 = []
print("Primeira lista (8 elementos):")
for i in range(8):
    while True:
        try:
            num = int(input(f"Elemento {i+1}: "))
            lista1.append(num)
            break
        except ValueError:
            print("Digite apenas números inteiros!")

# 2. Preencher a segunda lista
lista2 = []
print("\nSegunda lista (8 elementos):")
for i in range(8):
    while True:
        try:
            num = int(input(f"Elemento {i+1}: "))
            lista2.append(num)
            break
        except ValueError:
            print("Digite apenas números inteiros!")

# 3. Encontrar elementos comuns
comuns = []

for elemento in lista1:
    if elemento in lista2 and elemento not in comuns:
        comuns.append(elemento)

# 4. Mostrar resultados
print("\n" + "="*50)
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Elementos comuns às duas listas:", comuns)

if not comuns:
    print("(Não existem elementos em comum)")
else:
    print(f"Total de elementos comuns: {len(comuns)}")