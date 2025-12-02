print("Igor Freitas da Silva - 0220482523011 - sei la, pão")

padquali = 50.0
limitdesvio = 10.0
desvios_registrados = []
dias_consecutivos_baixo_padrao = 0
soma_desvios = 0
contador = 0
while input("Registrar uma medida de peça? (sim/outra coisa para termianr): ").lower() == "sim":
    medida = float(input("Insira a medida da peça: "))
    desvios_registrados.append(medida)
    desvio = abs(medida - padquali)
    if desvio > limitdesvio:
        dias_consecutivos_baixo_padrao += 1
        if dias_consecutivos_baixo_padrao == 3:
            print("ALERTA MÁXIMO! Produção Paralisada por Risco de Qualidade!")
            break
    else:
        dias_consecutivos_baixo_padrao = 0
for x in range(len(desvios_registrados)):
        desvio_atual = abs(desvios_registrados[x] - padquali)
        soma_desvios += desvio_atual
        contador += 1
media_desvio = soma_desvios / contador
print(f"A média dos desvios foi {media_desvio}.")

if dias_consecutivos_baixo_padrao == 3:
    print("Motivo de termino: Produção paralizada")
else:
     print("Motivo de termino: Produção acabou normalmente")