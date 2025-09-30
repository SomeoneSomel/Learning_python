vlrcom = float(input("Valor da compra: "))

if vlrcom > 100:
    desconto = 0.05
    vlrdes = vlrcom - (vlrcom * desconto)
    if vlrdes > 150:
        desadc = 0.02
        vlrdesdes = vlrdes - (vlrdes * desadc)
        vlrfinal = vlrdesdes
    else:
        vlrfinal = vlrdes
else:
    vlrfinal = vlrcom
    print("Nenhum desconto pode ser dado.")

print(f"O valor a ser pago é R${vlrfinal}!")