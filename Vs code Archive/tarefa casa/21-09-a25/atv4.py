pln = input("Selecione o plano desejado(Basíco, Padrão ou Premium): ").lower()
temp = int(input("O tempo da assinatura em meses: "))

print("")
if pln == "premium" or pln == "padrão":
    if temp >= 12 and temp <= 24:
        print("Parabéns! Você tem direito a um desconto de 15%")
    else:
        print("Seu plano é elegível, mas você não atende ao tempo de uso necessário para o desconto.")
else:
    print("Seu plano não é elegível para este desconto")