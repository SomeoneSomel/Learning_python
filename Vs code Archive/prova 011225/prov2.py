print("Igor Freitas da Silva - 0220482523011 - sei la, pão")

registro_temperaturas = []
contador_dias_criticos = 0
while input("Irá inserir a temperatura de um dia? (sim/não): ").lower() == "sim":
    temp = float(input("Insira a temperatura registrada: "))
    registro_temperaturas.append(temp)
for x in range(len(registro_temperaturas)):
    if registro_temperaturas[x] > 30:
        print("Alerta Quente!")
        contador_dias_criticos = contador_dias_criticos + 1
    elif registro_temperaturas[x] < 10:
        print("Alerta Frio!")
        contador_dias_criticos = contador_dias_criticos + 1
    else:
        print("Temperatura Agradável.")
print(f"As temperaturas registradas foram {registro_temperaturas}. Teve um total de {contador_dias_criticos} dia(s) críticos.")

    