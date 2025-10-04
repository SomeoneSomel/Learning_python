i = int(input("Diga sua idade: "))
peso = float(input("Diga seu peso: "))
cond = input("Qual sua condição?(Boa ou Ruim): ").lower()

print("")
if i >= 18 and peso >= 50:
    if cond == "boa":
        print("Você está elegível para doar sangue!")
    else:
        print("Você não pode doar sangue devido à sua condição de saúde.")
else:
    print("Você não está elegível para doar sangue. Verifique os requisitos de idade e peso")
