cfix = 500
cmat = float(input("O custo da materia-prima: "))
for x in range(1, 101):
    dm = cmat * 0.05
    custovariavel = cmat + dm
custo_total = cfix + custovariavel

if custo_total < 3000:
    margem = 0.35
elif custo_total >= 3000 and custo_total <= 5000:
    margem = 0.20
else:
    margem = 0.15
Preco_Minimo = (custo_total / 100) * (1 + margem)
margemp = margem * 100
print(f"O custo total da produção é {custo_total}, a margem de lucro aplicada foi {margemp}%, assim, o preço minimo a ser vendido é R${Preco_Minimo}")