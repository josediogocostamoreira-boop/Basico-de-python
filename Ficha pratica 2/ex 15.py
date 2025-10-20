#numeros

a = int(input("insira um numero: "))
b = int(input("insira um numero: "))
c = int(input("insira um numero: "))

#operação

operacao = input("insira se quer os numeros de forma crescente ou decrescente: ")

#crescente

if operacao == "crescente":
    if a < b and a < c:
        if b < c:
            print(a, b, c)
        else:
            print(a, c, b)
    if b < a and b < c:
        if a < c:
            print(b, a, c)
        else:
            print(b, c, a)
    if c < a and c < b:
        if a < b:
            print(c, a, b)
        else:print(c, b, a)

#decrescente

if operacao == "decrescente":
    if a > b and a > c:
        if b > c:
            print(a, b, c)
        else:
            print(a, c, b)
    if b > a and b > c:
        if a > c:
            print(b, a, c)
        else:
            print(b, c, a)
    if c > a and c > b:
        if a > b:
            print(c, a, b)
        else:print(c, b, a)

