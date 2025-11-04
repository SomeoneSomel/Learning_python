simb = input("Digite um simbolo (ex: *, !, @): ")
repitir = "sim"

while repitir == "sim":
    print(simb * 20)
    repitir = input("Deseja ver outra linha? (Digite SIM para continuar): ").lower()

print("")
print("Gerador encerrado. Obrigado!")