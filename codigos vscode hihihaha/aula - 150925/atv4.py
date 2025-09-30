idademn = 60
nacmn = "brasileiro"
idadeusu = int(input("Qual sua idade: "))
nacusu = input("Qual sua nacionalididade: ").lower()


if idadeusu >= idademn:
    if nacusu == nacmn:
        print("Você tem direito ao desconto especial!!")
    else:
        print("Você tem direito do desconto padrão.")
else:
    print("Você não tem direito de desconto.")