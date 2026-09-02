import os
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    try:
        num1 = float(input("Digite o SALDO disponível: "))
        num2 = float(input("Digite o VALOR que deseja SACAR: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"O SALDO disponível é: R$ {num1:.2f}")
        print(f"O VALOR que deseja SACAR é: R$ {num2:.2f}")
        if num1 >= num2:
            saldo_restante = num1 - num2
            print(f"O saldo restante após o saque é: R$ {saldo_restante:.2f}")
        else:
            print("Erro: Saldo insuficiente para o saque.")
    except ValueError:
        print("Erro: Por favor, digite apenas valores numéricos válidos.")