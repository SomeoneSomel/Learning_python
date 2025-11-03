import math

cnt = int(input("A quantidade a ser analisada: "))
soma_dos_quadrados = 0
cnt = cnt + 1
for x in range(1, cnt):
    square = math.pow(x, 2)
    if x % 3 == 0:
        print(f"{x} é múltiplo de 3")
    elif x % 2 == 0:
        print(f"{x} é par. Quadrado acumulado")
        soma_dos_quadrados = soma_dos_quadrados + square
    else:
        print(f"{x} é ímpar. Ignorado.")
print(f"O valor final da soma de todos os quadrados é {soma_dos_quadrados}")
