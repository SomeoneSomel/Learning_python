qtprod = int(input("A quantidade de produtos diferentes a ser comprado: "))
qtprod = qtprod + 1
ttcom = 0

for i in range(1,qtprod):
    i = float(input(f"O preço do {i}° produto: "))
    ttcom = ttcom + i
print(f"O preço total a ser pago é R${ttcom}")