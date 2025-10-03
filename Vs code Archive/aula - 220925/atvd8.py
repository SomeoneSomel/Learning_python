tmpizza = input("Tamanho da pizza(Pequena, média ou grande): ").lower()
sab = int(input("Quantiddes de sabores: "))
status = input("Status do cliente(Vip ou normal): ").lower()

print("")
if tmpizza == "grande" and sab > 2:
    print("Pedido especial: sujeito a taxa extra.")
elif tmpizza == "grande" or status == "vip":
    print("Pedido prioritário: prepare para entrega rápida.")
elif tmpizza == "média" and sab == 1:
    print("Pedido padrão: processamento normal")
else:
    print("Pedido de baixo volume: pode ser processado a qualquer momento.")
    print("")
