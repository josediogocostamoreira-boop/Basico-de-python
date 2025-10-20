#menu

criar = 1

atualizar = 2

eleminar = 3

sair = 4

#selecionar

operação = int(input("digite 1 para criar, digite 2 para atualizar, digite 3 para eleminar, digite 4 para sair: "))

if operação == criar: print("criar pasta")

if operação == atualizar: print("atualizar pasta")

if operação == eleminar: print("eleminar pasta")

if operação == sair: print("")

if operação >= 5: print("operação invalida")
