# variaveis
c=0
s=0

#introduzir numeros -1 para parar e calcular a media dos numeros introduzidos
n=int(input("Introduza um número (-1 para terminar): "))
while n!=-1:
    s=s+n
    c=c+1
    n=int(input("Introduza um número (-1 para terminar): "))
m=s/c
print("Média dos números introduzidos:",m)
