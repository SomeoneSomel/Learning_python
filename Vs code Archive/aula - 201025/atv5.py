qnf = int(input("A quantidade de notas fiscais a ser processada: "))
soma_das_notas = 0.0
qnf = qnf + 1
for x in range(1, qnf):
    nf = float(input(f"O valor da {x}° nota fiscal: "))
    soma_das_notas = soma_das_notas + nf
if soma_das_notas <= 1000:
    al = 0.05
elif soma_das_notas > 1000 and soma_das_notas <= 4999:
    al = 0.09
elif soma_das_notas >= 5000 and soma_das_notas <=14999:
    al = 0.12
else:
    al = 0.16
valor_imposto = soma_das_notas * al
alp = al * 100
print(f"O valor total das notas é R${soma_das_notas}. Com uma aliquota de {alp}%, o valor total é R${valor_imposto}.")
