#numero

numero = int(input("insira um numero: "))

#valor

valor = 2

#numeros pares do numero inserido

while valor < numero:
    if numero % 2 == 0:
        print(numero)
    numero = numero - 1

