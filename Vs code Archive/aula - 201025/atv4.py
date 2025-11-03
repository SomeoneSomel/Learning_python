mestol = int(input("Total de meses a serem analisados: "))
consumo_total_kwh = 0.0
valor_total_pago = 0.0
mestolfor = mestol + 1
for x in range(1, mestolfor):
    conkwh = float(input(f"A quantidade de kwh de gastos no {x}° mês: "))
    if conkwh <= 100:
        taf = 0.55
    elif conkwh > 100 and conkwh <= 200:
        taf = 0.70
    else:
        taf = 0.90
    cmens = conkwh * taf
    consumo_total_kwh = consumo_total_kwh + conkwh
    valor_total_pago = valor_total_pago + cmens
media_Mensal = consumo_total_kwh / mestol
if media_Mensal > 180:
    print("Alerta! O consumo médio está elevado. Sugerir medidas de economia")
else:
    print("Consumo médio dentro dos limites normais")
print(f"O consumo total em kWh é {consumo_total_kwh} e o valor pago ao total é {valor_total_pago}")
