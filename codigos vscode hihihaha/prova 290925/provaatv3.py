print("Igor freitas da silva - 0220482523011 - sei lá, pão.")
#Igor freitas da silva - 0220482523011 - sei lá, pão.

psen = float(input("O Peso da encomenda(em kg): "))
dsen = float(input("A Distancia da encomenda(em km): "))
cstbase = (psen * 1.5) + (dsen * 0.25)

if cstbase > 200:
    dsct = cstbase - (cstbase * 0.10)
    print(f"O valor base é de R${cstbase} e o valor final com descontos/acrescimos já aplicado é de R${dsct}.")
elif cstbase > 50 and cstbase < 200:
    print(f"O valor base é de R${cstbase}. Nenhum desconto foi aplicado.")
elif cstbase < 50:
    vlrf = cstbase + 5
    print(f"O valor base é de R${cstbase} e o valor final com descontos/acrescimos já aplicado é de R${vlrf} ")