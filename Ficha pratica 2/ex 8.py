#Notas

nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
nota3 = int(input("Digite sua terceira nota: "))

#Calculo da media

media = int(nota1 + nota2 + nota3) / 3
print("a media é: ", media)

#media ponderada

mediaPonderada = (nota1*0.25 + nota2*0.35 +nota3*0.40)
print("a media ponderada é: ", mediaPonderada)

if mediaPonderada >= 9.5:
    print("o aluno passou com:", mediaPonderada,"de media")
else: print("o aluno não passou")