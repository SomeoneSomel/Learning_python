import math

la = float(input("Lado a do triangulo: "))
lb = float(input("Lado b do triangulo: "))
lc = float(input("Lado c do triangulo: "))
ltri = la + lb
cosseno_gama = (la**2 + lb**2 - lc**2) / (2 * la * lb)

if ltri > lc:
    math.degrees(math.acos(cosseno_gama))    
    if cosseno_gama == 90:
        print("Triângulo Retângulo")
    elif cosseno_gama < 90:
        print("Triângulo Acutângulo")
    elif cosseno_gama > 90:
        print("Triângulo Obtusângulo")
else:
    print("Não é um triângulo")

