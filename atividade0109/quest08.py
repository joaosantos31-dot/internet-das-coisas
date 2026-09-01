import os
os.system("cls")
notas = []
while True:
    os.system("cls")
    if notas:
        print("--- Notas Cadastradas ---")
        for idx, item in enumerate(notas, start=1):
            print(f"{idx}ª nota: {item}")
        print("-------------------------\n")
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)
os.system("cls")
if notas:
    quantidade = len(notas)
    media = sum(notas) / quantidade
    maior = max(notas)
    menor = min(notas)
    notas.sort(reverse=True)
    print("=== RELATÓRIO DE NOTAS ===")
    print("\nNotas cadastradas:")
    for idx, item in enumerate(notas, start=1):
        print(f"{idx}ª nota: {item}")
    print("--------------------------")
    print(f"Quantidade de notas: {quantidade}")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Notas em ordem decrescente: {notas}")
else:
    print("Nenhuma nota foi cadastrada.")