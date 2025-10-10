qntf = int(input("A quantidade de notas fiscais: "))
soma_das_notas = 0.0
qntf = qntf + 1
for x in range(1, qntf):
    x = input(f"O valor da {x}° nota: ")
    soma_das_notas = soma_das_notas + x

if soma_das_notas <= 1000:
    al = 0.05
    vlrimp = soma_das_notas * al
elif soma_das_notas > 1000 and soma_das_notas <= 4999:
    al = 0.09
    vlrimp = soma_das_notas * al
elif soma_das_notas >= 5000 and soma_das_notas <= 14999:
    al = 0.12
    vlrimp = soma_das_notas * al
else:
    al = 0.16
    vlrimp = soma_das_notas * al
print(f"O valor total do imposto é {vlrimp} e o valor da aliquota é {al}. O valor das notas foi {soma_das_notas}.")