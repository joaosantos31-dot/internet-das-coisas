import os
os.system("cls")
import random
numero_secreto = random.randint(1, 20)
tentativas = 0
dica = ""
while True:
    os.system("cls")
    print("=== JOGO DA ADIVINHAÇÃO ===")
    print("Tente adivinhar o número entre 1 e 20!")
    print(f"Tentativas realizadas: {tentativas}")
    print("===========================")
    if dica:
        print(f"\nDica: {dica}\n")
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1
    if palpite == numero_secreto:
        os.system("cls")
        print("=== PARABÉNS! VOCÊ ACERTOU! ===")
        print(f"O número secreto era: {numero_secreto}")
        print(f"Total de tentativas: {tentativas}")
        break
    elif palpite < numero_secreto:
        dica = f"O número secreto é MAIOR que {palpite}."
    else:
        dica = f"O número secreto é MENOR que {palpite}."