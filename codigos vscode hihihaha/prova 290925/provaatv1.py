print("Igor freitas da silva - 0220482523011 - sei lá, pão.")
#Igor freitas da silva - 0220482523011 - sei lá, pão.

pcost = float(input("O preço do custo do produto: "))
psell = float(input("O preço de venda do produto: "))
pleft = pcost - psell
m = (pleft / pcost) * 100
if m > 30:
    print("Margem Excelente")
elif m >= 10 and m <= 30:
    print("Margem Satisfatória")
elif m < 10:
    print("Margem Baixa: Avaliar preço de venda")
