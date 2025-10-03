print("Igor freitas da silva - 0220482523011 - sei lá, pão.")
#Igor freitas da silva - 0220482523011 - sei lá, pão.

vlrgli = float(input("Valor da glicose durante o jejum em mg/DL: "))

if vlrgli < 100:
    print("Glicemia Normal")
elif vlrgli >= 100 and vlrgli <= 125:
    print("Pré-diabetes: Risco Moderado")
elif vlrgli > 125:
    print("Diabetes: Nível Alto.")