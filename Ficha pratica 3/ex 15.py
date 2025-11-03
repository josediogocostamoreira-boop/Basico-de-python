#inserir numero
num = int(input("Insira um número para calcular o fatorial: "))
fatorial = 1

#calculo do fatorial
while (num > 0):
    fatorial = fatorial * num
    num -= 1

#resultado
print("Fatorial:", fatorial)