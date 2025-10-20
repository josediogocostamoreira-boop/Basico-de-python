valor = int(input("Valor: "))

if (valor % 5 == 0):  # Múltiplo de 5

    # Notas 200€
    notas = valor // 200
    print("Notas 200€:", notas)

    valor = valor % 200

    # Notas 100€
    notas = valor // 100
    print("Notas 100€:", notas)

    valor = valor % 100

    # Notas 50€
    notas = valor // 50
    print("Notas  50€:", notas)

    valor = valor % 50

    # Notas 20€
    notas = valor // 20
    print("Notas  20€:", notas)

    valor = valor % 20

    # Notas 10€
    notas = valor // 10
    print("Notas  10€:", notas)

    valor = valor % 10

    # Notas 5€
    notas = valor // 5
    print("Notas   5€:", notas)

else:
    print("Valor inválido. Não temos trocos!")