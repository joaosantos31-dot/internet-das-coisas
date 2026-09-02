import os
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    try:
        num1 = float(input("Digite a primeira nota: "))
        num2 = float(input("Digite a segunda nota: "))
        num3 = float(input("Digite a terceira nota: "))
        soma = num1 + num2 + num3
        media = soma / 3
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"A primeira nota digitada foi: {num1}")
        print(f"A segunda nota digitada foi: {num2}")
        print(f"A terceira nota digitada foi: {num3}")
        if media>=7:
            print(f"A 1º nota digitada foi: {num1}")
            print(f"A 2º nota digitada foi: {num2}")
            print(f"A 3º nota digitada foi: {num3}")
            print(f"A média das notas digitadas foi: {media:.2f}")
            print("Você foi aprovado.")
        elif media<=6.9 and media>=5:
            print(f"A 1º nota digitada foi: {num1}")
            print(f"A 2º nota digitada foi: {num2}")
            print(f"A 3º nota digitada foi: {num3}")
            print(f"A média das notas digitadas foi: {media:.2f}")
            print("Você está em recuperação.")
        elif media<5 and media>=0:
            print(f"A 1º nota digitada foi: {num1}")
            print(f"A 2º nota digitada foi: {num2}")
            print(f"A 3º nota digitada foi: {num3}")
            print(f"A média das notas digitadas foi: {media:.2f}")
            print("Você foi reprovado.")
        else:
            print("Erro: Por favor, digite uma nota válida.")
    except ValueError:
        print("Erro: Por favor, digite apenas notas válidas.")