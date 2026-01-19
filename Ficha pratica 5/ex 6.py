lista = []
tamanho = 10

print("Insira 10 números:")

for i in range(tamanho):
    numero = int(input(f"Digite o número {i+1}/10: "))
    lista.append(numero)

# Agora verificamos se a lista é crescente, decrescente ou nenhum dos dois
crescente = True
decrescente = True

for i in range(1, len(lista)):
    if lista[i] > lista[i-1]:
        decrescente = False  # não pode ser decrescente
    elif lista[i] < lista[i-1]:
        crescente = False   # não pode ser crescente
    # se lista[i] == lista[i-1], ambos continuam True por enquanto (crescente/decrescente não estrito)

if crescente and decrescente:
    print("A lista é constante (todos os números iguais)")
elif crescente:
    print("A lista é crescente (não decrescente)")
    print("Lista:", lista)
elif decrescente:
    print("A lista é decrescente (não crescente)")
    print("Lista:", lista)
else:
    print("A lista não é crescente nem decrescente")
    print("Lista:", lista)









