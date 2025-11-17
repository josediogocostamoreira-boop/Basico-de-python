repetir="s"

while repetir!="s":
    # Ler os dois valores
    num1 = float(input("Introduza o primeiro valor: "))
    num2 = float(input("Introduza o segundo valor: "))

    # Ler a operação
    operacao = input("Introduza a operação (+, -, *, /): ")

    # Calcular conforme a operação
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero!")
            continue
    else:
        print("Operação inválida!")
        continue

    # Mostrar o resultado
    print(f"Resultado: {resultado}")

    # Perguntar se deseja continuar
    repetir = input("Deseja continuar? (introduza s/n): ")


print("Programa terminado.")