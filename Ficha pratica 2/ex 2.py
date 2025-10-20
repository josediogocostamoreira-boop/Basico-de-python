#salario

salario = int(input("introduza o seu salário: "))

#taxa

taxa30 = salario * 0.30
taxa20 = salario * 0.20

#valor a pagar

if (salario >= 15000): print("a taxa é:", taxa30)

else:
    print("a taxa é: ", taxa20)