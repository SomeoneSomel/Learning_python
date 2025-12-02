#Prova
print("Igor Freitas da Silva - 0220482523011 - sei la, pão")
gastos_semanais = []
continuar = "sim"
somar = 0
while continuar.lower() == "sim":
    gasto = float(input("Insira o gasto: R$"))
    gastos_semanais.append(gasto)
    continuar = input("Adcionar outro valor? (sim/não): ")
for x in range(len(gastos_semanais)):
    somar += gastos_semanais[x]

print(f"Todos os gastos foram {gastos_semanais}, que somando dá R${somar}")
