tab = int(input("A tabuada que deseja ver: "))
contador = 1
print("")
while contador <= 10:
    resultado = tab * contador
    print(f"{tab} x {contador} = {resultado}")
    contador += 1

print("")
print("Tabuada completa!")
