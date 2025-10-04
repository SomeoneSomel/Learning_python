cndtem = input("Insira a condição do tempo(Limpo, nublado ou tempestade): ").lower()
vspt = int(input("Insira a distancia que é possível ver da pista em metros: "))
status = input("Insira a condição do motor(Ok ou Avaria): ").lower()

print("")
if cndtem == "limpo" and vspt > 1000:
    print("Condições de decolagem ideais. Autorizado")
elif cndtem == "nublado" and vspt >= 500:
    print("Condições de decolagem aceitáveis. Aguardando autorização final.")
elif status == "avaria":
    print("Decolagem negada. Avaria no motor detectada.")
else:
    print("Condições de segurança não atendidas. Voo atrasado.")