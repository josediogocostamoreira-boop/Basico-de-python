#numeros
a = int(input("insira um numero"))
b = int(input("insira um numero"))
c = int(input("insira um numero"))

#ordem crescente

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
        print(c, b, a)
    else:
        print(c, a, b)





