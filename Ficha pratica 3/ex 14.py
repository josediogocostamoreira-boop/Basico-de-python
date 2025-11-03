#quantos numeros é para inserir
quantidadeNumeros = int(input("Quantos números deseja inserir: "))
numerosInseridos = 1

#inserir numero
numAnt = int(input("Insira um número: "))

#a ordem é crescente o não
crescente = True

while (numerosInseridos < quantidadeNumeros):
    numAtual = int(input("Insira um número: "))
    numerosInseridos += 1

    if (numAtual <= numAnt):
        # Deixa de ser crescente
        crescente = False

    numAnt = numAtual


if (crescente):  # crescente == True
    print("Crescente")
else:
    print("Não Crescente")