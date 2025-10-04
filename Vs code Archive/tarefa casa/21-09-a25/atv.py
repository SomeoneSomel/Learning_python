i = int(input("Qual sua idade: "))
exp = int(input("Quantos anos de experiencia: "))
disp = input("Qual sua disponibilidade?(Manhã ou tarde)").lower()

print("")
if i > 18 and exp > 1:
    if disp == "manhã" or disp == "tarde":
        print("Parabéns, você está elegivel a vaga!")
    else:
        print("Não elegível: Disponibilidade não corresponde aos requisitos")
else:
    print("Não elegível: Idade ou experiência insuficientes.")