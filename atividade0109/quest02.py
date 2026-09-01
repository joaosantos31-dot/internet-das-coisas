import os
os.system("cls")
quant=5
lista=[]
for i in range(quant):
    os.system("cls")
    for x in range(len(lista)):
        print(f"{x+1}º produto {lista[x]}")
    a=input(f"Digite o produto {i+1}:\n")
    lista.append(a)
os.system("cls")
print("= = = LISTA DE PRODUTOS: = = =")
for x in range(len(lista)):
    print(f"{x+1}º produto {lista[x]}")