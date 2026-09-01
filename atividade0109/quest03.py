import os
os.system("cls")
quant=6
lista_numeros=[]
for i in range(quant):
    os.system("cls")
    for x in range(len(lista_numeros)):
        print(f"{x+1}º número {lista_numeros[x]}")
    num=int(input(f"Digite o {i+1}º número inteiro: "))
    lista_numeros.append(num)
os.system("cls")
soma=sum(lista_numeros)
maior=max(lista_numeros)
menor=min(lista_numeros)
lista_numeros.sort
print("\n--- RESULTADOS ---")
print(f"Soma dos números: {soma}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Lista dos números cadastrados:")
for y in range(len(lista_numeros)):
    print(f"{y+1}º número: {lista_numeros[y]}")