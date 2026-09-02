import os
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    try:
        idade = float(input("Digite a idade: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if idade>= 18:
            print(f"A idade digitada foi: {idade}")
            print("Você é maior de idade.")
        elif idade>=0:
            print(f"A idade digitada foi: {idade}")
            print("Você é menor de idade.")
        else:
            print("Erro: Por favor, digite uma idade válida.")
    except ValueError:
        print("Erro: Por favor, digite uma idade válida.")