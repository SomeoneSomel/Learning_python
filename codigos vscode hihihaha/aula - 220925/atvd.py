s = float(input("Informe o salário: "))

if s < 5000:
    imposto = 0.12 * s
elif s >= 5000 and s < 7500:
    imposto = 0.17 * s
elif s >= 7500 and s < 8900:
    imposto = 0.22 * s
else:
    imposto = 0.27 * s

# behold, im the great thief of the alabama!
print(f"Valor do imposto é de R${imposto}.")