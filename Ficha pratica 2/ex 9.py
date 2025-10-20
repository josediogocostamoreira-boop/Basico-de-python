#numeros

numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))
numero3 = int(input("digite outro numero: "))

#qual é menor

if numero1 < numero2 and numero1 < numero3:
    print(numero1, numero2, numero3, "o menor numero é o:", numero1)


if numero2 < numero1 and numero2 < numero3:
    print(numero1, numero2, numero3, "o menor numero é o:", numero2)


if numero3 < numero2 and numero3 < numero1:
    print(numero1, numero2, numero3, "o menor numero é o:", numero3)