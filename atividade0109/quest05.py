import os
nomes = []
while True:
    os.system("cls")
    if nomes:
        print("--- Nomes Cadastrados ---")
        for idx, item in enumerate(nomes, start=1):
            print(f"{idx}. {item}")
        print("-------------------------\n")
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    nomes.append(nome)
nomes.sort()
os.system("cls")
print("--- RESULTADO FINAL ---")
print(f"Total de nomes cadastrados: {len(nomes)}")
print("Lista em ordem alfabética:")
for idx, nome in enumerate(nomes, start=1):
    print(f"{idx}. {nome}")