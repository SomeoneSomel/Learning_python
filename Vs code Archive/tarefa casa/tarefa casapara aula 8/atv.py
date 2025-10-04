tmp = input("Insira a condição do tempo(Limpo, nublado ou tempestade): ").lower()
visp = int(input("Insira a visibilidade da pista em metros: "))
status = input("Insira a condição do motor(Ok ou avaria): ").lower()

if tmp == "limpo" and visp > 1000:
    print("Condições de decolagem ideais. Autorizado.")
elif tmp == "nublado" and visp >= 500 and status == "ok":
    print("Condições de decolagem aceitáveis. Aguardando autorização final.")
elif status == "avaria":
    print("Decolagem negada. Avaria no motor detectada.")
else:
    print("Condições de segurança não atendidas. Voo atrasado.")