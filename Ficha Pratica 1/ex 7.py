#produtos

produto1 = int(input("Digite o valor do primeiro produto: "))
produto2 = int(input("Digite o valor do segundo produto: "))
produto3 = int(input("Digite o valor do terceiro produto: "))

#Valor a pagar

desconto = (produto1 + produto2 + produto3) * 0.1
pagamento = (produto1 + produto2 + produto3) - desconto


print("o valor a pagar é :", pagamento)


