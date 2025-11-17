# Ler o número do utilizador
n = int(input("Introduza um número: "))

soma = 0
i = 1

# Soma números consecutivos até ultrapassar ou igualar n
while soma < n:
    soma += i
    i += 1

# Verifica se é triangular
if soma == n:
    print(f"{n} é um número triangular.")
else:
    print(f"{n} não é um número triangular.")