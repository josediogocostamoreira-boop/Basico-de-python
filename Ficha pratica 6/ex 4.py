alunos = {
"João": [8,7,9],
"Maria": [16,19,18],
"Ana": [19,18,20]

}

print(alunos)

conta = input("insira o nome do aluno ")

if conta == "João":
    media = int(sum(alunos["João"])/ len(alunos["João"]))
    print(media)
if conta == "Maria":
    media = int(sum(alunos["Maria"])/ len(alunos["Maria"]))
    print(media)
if conta == "Ana":
    media = int(sum(alunos["Ana"])/ len(alunos["Ana"]))
    print(media)