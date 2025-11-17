# Jogador 1 introduz o número secreto
numero_secreto = int(input("Jogador 1, introduza um número entre 0 e 100: "))

# Verifica se o número está dentro dos limites
while numero_secreto < 0 or numero_secreto > 100:
    numero_secreto = int(input("Valor inválido! Introduza um número entre 0 e 100: "))

# Limpa o ecrã (opcional, apenas visual)
print("\n" * 50)
print("Agora é a vez do Jogador 2!")

tentativas = 0
acertou = False

# Jogador 2 tenta adivinhar
while not acertou:
    palpite = int(input("Jogador 2, tenta adivinhar o número: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Demasiado baixo! Tenta um número mais alto.")
    elif palpite > numero_secreto:
        print("Demasiado alto! Tenta um número mais baixo.")
    else:
        acertou = True
        print(f"🎉 Acertaste! O número era {numero_secreto}.")
        print(f"Precisaste de {tentativas} tentativas.")