#salario

salario = int(input("introduza o seu salário: "))

#taxa

taxa30 = salario * 0.30
taxa20 = salario * 0.20
taxa35 = salario * 0.35
taxa40 = salario * 0.40

#valor a pagar

if (salario <= 15000):
    print("a taxa é 20%:", taxa20)

if (salario > 15000 and salario <=20000):
    print("a taxa é 30%:", taxa30)

if (salario >20000 and salario <= 25000):
    print("a taxa é 35%:", taxa35)

if (salario >25000):
    print("a taxa é 40%: ", taxa40)



