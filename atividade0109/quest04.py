import os
os.system("cls")
pares=[]
impares=[]
pares_num = 0
impares_num = 0
lista=[12, 7, 9, 20, 31, 44, 18, 5]
for x in lista:
    if x % 2 == 0:
        pares_num += 1
        pares.append(x)
    else:
        impares_num += 1
        impares.append(x)
print(f"Quantidade de números pares: {pares_num}")
print(f"Quantidade de números impares: {impares_num}")
print("= LISTA DE NÚMEROS PARES =")
for i in range(len(pares)):
    print(f"{i+1}º número par: {pares[i]}")
print("\n=== LISTA DE NÚMEROS ÍMPARES ===")
for i in range(len(impares)):
    print(f"{i+1}º número ímpar: {impares[i]}")