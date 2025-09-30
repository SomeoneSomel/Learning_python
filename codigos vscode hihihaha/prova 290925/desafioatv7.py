print("Igor freitas da silva - 0220482523011 - sei lá, pão.")
#Igor freitas da silva - 0220482523011 - sei lá, pão.

pu = float(input("A pureza do lote(em decimal): "))
mt = float(input("A massa total do lote(em kg): "))
txcont = float(input("A taxa de contaminação(em decimal): "))
fd = (pu * 100) - (txcont * 50)

if mt > 1000:
    pb = 10
else:
    pb = 12.50

if fd > 90 and pu > 0.98:
    print("Classificação: PREMIUM (Venda Imediata)")
    p_final_kg = pb * 1.50
elif fd > 70 and fd < 90 and txcont < 0.05:
    print("Classificação: PADRÃO (Venda Normal)")
    p_final_kg = pb * 1.10
elif fd < 70 or pu < 0.90:
    print("Classificação: REPROVADO (Descarte ou Re-processamento)")
    p_final_kg = pb * 0.25
else:
    print("Classificação: ACEITÁVEL (Margem Mínima)")
    p_final_kg = pb * 0.90

precototal = p_final_kg * mt
precototalr = round(precototal)

print(f"O preço por lote é R${pb}. O preço final, com qualquer desconto/acrescimo é R${precototalr}")
