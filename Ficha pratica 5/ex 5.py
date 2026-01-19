#abre lista
lista = []
numero = int(input("insira um numero: "))

#variaveis auxiliares
contador = 0
soma = 0

#enquanto numero for maior ou igual a 0 continua a introduzir numeros
while numero >= 0:
    lista.append(numero)
    soma = soma + numero  #soma de todos os numeros
    contador = contador + 1
    numero = int(input("insira um numero: "))

print(lista)

#calculo da media
media = soma / contador
print("a media é: ", media)

