salbase = 800
limitf = 1
contf = 0
pdiat = 0
for x in range (1, 6):
    pdia = int(input(f"A produtividade do dia {x} (0 a 100): "))
    if pdia < 60:
        contf = contf + 1
    pdiat = pdiat + pdia
produtimdia = pdiat / 5.
if produtimdia > 80 and contf <= 1:
    print("Pagamento Máximo: Bônus de 10% aplicado.")
    Pagfinal = salbase * 1.10
elif produtimdia >= 60 and produtimdia <= 80:
    print("Pagamento Padrão: Penalidade de 5% aplicada (Devido a falhas)")
    Pagfinal = salbase * 0.95
else:
    print("Penalidade Severa: Pagamento reduzido em 25%")
    Pagfinal = salbase * 0.75
print(f"A produtividade média é de {produtimdia}, a contagem de falhas é {contf} e o pagamento final é {Pagfinal}")