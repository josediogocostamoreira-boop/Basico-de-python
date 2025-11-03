#inicio
inicio = int(input("insira um valor de começo:"))

#limite
limite = int(input("insira um valor limite: "))

#operação
while inicio <= limite:
    inicio = inicio +1
    if inicio % 5 == 0:
        print(inicio)