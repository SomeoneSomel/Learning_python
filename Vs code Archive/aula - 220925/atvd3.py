ting = input("Seu tipo de ingresso(Padrão ou Premium): ").lower()
i = int(input("Sua idade: "))
listvip = input("Participa da lista VIP?(Sim ou não): ").lower()

print("")
if ting == "premium":
    print("Acesso total: todas as áreas e benefícios especiais")
elif i >= 18 and listvip == "sim":
    print("Acesso VIP: área exclusiva e entrada prioritária.")
elif i >= 18 or ting == "padrão":
    print("Acesso padrão: entrada para a área principal do evento.")
else:
    print("Acesso negado: verifique os critérios de entrada.")
