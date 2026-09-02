import os
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"O primeiro número digitado foi: {num1}")
        print(f"O segundo número digitado foi: {num2}")
        if soma.is_integer():
            soma = int(soma)
            print(f"A soma de {num1} e {num2} é: {int(soma)}")
        else:
            print(f"A soma de {num1} e {num2} é: {soma}")
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")