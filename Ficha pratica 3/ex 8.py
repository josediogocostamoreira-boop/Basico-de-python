#numeros
numero1 = int(input("diga um valor: "))

numero2 = numero1

#repetição
repeticao = 0

#mostrar os 5 numeros anteriores
while repeticao < 5:
    numero1 = numero1 - 1
    repeticao += 1
    print(numero1)

numero1 = numero2

#mostrar os 5 numeros seguintes
while repeticao >0:
    numero1 += 1
    repeticao -=1
    print(numero1)
