qntdias = int(input("A quantidade de dias a ser analisado: "))
soma_das_temperaturas = 0.0
qntdias =  qntdias + 1
for x in range(1, qntdias):
    x = float(input(f"A temperatura do {x}° dia: "))
    soma_das_temperaturas = soma_das_temperaturas + x
qntdias = qntdias - 1
tempmed = soma_das_temperaturas / qntdias

if tempmed > 28:
    print("Média de temperatura: Clima Quente")
elif tempmed >=18 and tempmed <= 28:
    print("Média de temperatura: Clima Agradável")
else:
    print("Média de temperatura: Clima Frio")