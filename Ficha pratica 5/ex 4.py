#abre lista
lista = []

#lista com 10 numeros
for i in range(0,10):

    #insira um numero na lista
    numeroinserido = int(input ("insira um numero na lista:"))

    #lista acaba no numero inserido
    lista.append(numeroinserido)

    lista.sort()

    #print lista
    print (lista)

    #min(lista) = o numero menor da lista
    menor = min(lista)
    print (menor)