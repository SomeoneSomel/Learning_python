tab = int(input("A tabuada que deseja ver: "))
contador = 1

print("")
if tab >= 0: #doing a cheeky check for a negative number, idk i just want it to.
    while contador <= 10:
        resultado = tab * contador
        print(f"{tab} x {contador} = {resultado}")
        
        contador += 1
    print("")
    print("Tabuada completa!")
else: # if it is a negative number, i will just not do it, like a middle finger for the user lol.
    print("Numero negativo, a tabela não será completa.")