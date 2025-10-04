orc = float(input("Orçamento do projeto: "))
time = int(input("Tamanho da equipe: "))
arp = input("A área da pesquisa(Inovação ou sustentabilidade): ").lower()

print("")
if orc > 50000 and time > 3:
    if arp == "inovação" or arp == "sustentabilidade":
        print("Projeto qualificado para o financiamento!")
    else:
        print("Projeto não qualificado: A área de pesquisa não é prioritária.")
else:
    print("Projeto não qualificado: Orçamento ou tamanho da equipe insuficientes")