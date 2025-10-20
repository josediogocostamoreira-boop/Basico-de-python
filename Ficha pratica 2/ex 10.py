#variaveis

num1 = int(input("Introduza um numero: "))

num2 = int(input("Introduza um numero: "))

#calculadora

operacao = input("introduza a operação a fazer (+ - + /): ")
if operacao == "+":
    total = num1 + num2
    print(total)

if operacao == "-":
    total = num1 - num2
    print(total)

if operacao == "*":
    total = num1 * num2
    print(total)

if operacao == "/":
    total = num1 / num2
    print(total)

if operacao != "+" and operacao != "-" and operacao != "/" and operacao != "*":
    print("erro")