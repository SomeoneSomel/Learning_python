vlm = int(input("O volume das vendas: "))
taxsat = float(input("A taxa de satisfação do cliente: "))
meta = input("A meta de clientes novos foi atingida?(Sim ou não): ").lower()

print("")
if vlm >= 50000 and taxsat > 0.9:
    print("Vendedor de alta performance: classificado como Sênior.")
elif vlm >= 30000 and meta == "sim":
    print("Vendedor de bom desempenho: classificado como Pleno.")
elif taxsat >= 0.8 or meta == "sim":
    print("Vendedor em desenvolvimento: classificado como Júnior.")
else:
    print("Vendedor em revisão de desempenho: não atende aos critérios mínimos.")