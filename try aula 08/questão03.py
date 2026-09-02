import os
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    try:
        num1 = int(input("Digite um número inteiro: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"A tabuada do número {num1} é:")
        for i in range(1, 11):
            resultado = num1 * i
            print(f"{num1} x {i} = {resultado}")
    except ValueError:
        print("Entrada inválida!!!")
        print("Por favor, digite apenas números inteiros.")