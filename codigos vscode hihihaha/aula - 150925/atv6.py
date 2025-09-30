tmp = float(input("Temperatura lá fora em C°: "))
chovendoyn = input("Está chovendo lá fora? Sim ou não somente(gramatica tem que está correta!): ").lower()
if tmp >= 20 and chovendoyn == "não":
    print("O tempo está ideal atividades ao ar livre!")
else:
    if tmp >=15 and tmp <=20 or chovendoyn == "sim":
        print("Tempo não está ideal para atividades ao ar livre.")
    else:
        print("O tempo não está propicio para atividades ao ar livre!")
