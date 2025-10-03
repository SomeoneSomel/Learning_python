vct = float(input("Valor total da compra: "))
status = input("Status do cliente(Fiel ou Novo): ").lower()
tp = input("Tipo do produto(Eletrônico ou Livro): ").lower()

print("")
if vct >= 200 and status == "fiel":
    print("Parabéns! Você tem direito a frete grátis e um brinde especial.")
elif vct >= 200 or tp == "livro":
    print("Você tem direito a frete grátis. Aproveite!")
elif status == "fiel" and tp == "eletrônico":
    print("Você tem direito a um desconto de 5% no frete.")
else:
    print("Não há promoções aplicáveis a este pedido.")