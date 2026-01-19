#abre lista
lista = []

#variavel total
total = 0

#lista de tamanho 12
for i in range(0,12):

    #comissão retirada
    comissão = int(input("insira o valor da comissão: "))

    #valor que recebemos - comissão
    numeroinserido = int(input ("insira o valor que recebeu : ")) - comissão

    #lista acaba no numero insserido
    lista.append(numeroinserido)

    #imprime lista
    print(lista)

    #soma de todos os numeros
    total += numeroinserido


    #imprime soma
    print("soma:", total)

