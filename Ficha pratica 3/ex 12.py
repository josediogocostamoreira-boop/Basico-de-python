#variavel
numero= 0

#intervalos
numero1=0
numero2=0
numero3=0
numero4=0

#operação introduzir numeros e dizer quantos estão nos intervalos
while numero >= 0:
    numero = int(input("insira um valor:"))
    if numero > 0 and numero <= 25:
        numero1 = numero1 + 1
    if numero > 26 and numero <= 50:
        numero2 = numero2 + 1
    if numero > 51 and numero <= 75:
        numero3 = numero3 + 1
    if numero > 76 and numero <= 100:
        numero4 = numero4 + 1
    if numero < 0:
        print("intervalo de 0 a 25:",numero1,"intervalo de 26 a 50:",numero2,"intervalo de 51 a 75:",numero3,"intervalo de 76 a 100:", numero4)