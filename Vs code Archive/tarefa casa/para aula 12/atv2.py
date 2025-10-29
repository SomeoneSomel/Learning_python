numdias =   int(input("Digite o número de dias: "))
producao_total = 0
dias_acima_da_meta = 0
numdiasf = numdias + 1
for x in range(1, numdiasf):
    x = int(input(f"Digite a produção do {x}° dia: "))
    metadia = 50
    if x > metadia:
        dias_acima_da_meta = dias_acima_da_meta + 1
        producao_total = producao_total + x
media_diaria = producao_total / numdias
if metadia > 60 and dias_acima_da_meta >= 4:
    print("BÔNUS MÁXIMO! (15% sobre a produção total).")
    bonus = producao_total * 0.15
elif metadia > 50 or dias_acima_da_meta >- 3:
    print("BÔNUS PARCIAL! (5% sobre a produção total)")
    bonus = producao_total * 0.05
else:
    print("Sem Bônus. Metas de produtividade não foram atingidas")
    bonus = 0
print(f"A media diária de produção foi de {media_diaria} unidades. O valor final do bônus é R$ {bonus}")