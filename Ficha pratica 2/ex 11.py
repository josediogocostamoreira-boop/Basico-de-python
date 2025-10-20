#saldo

saldo = int(input("introduza o saldo médio:"))

#valor a debitar

debito = int(input("introduza o valor a debitar:"))

#operação

if saldo > debito: print("saldo atual:", saldo - debito)

if debito > saldo: print("saldo isuficiente", "saldo atual:", saldo)
