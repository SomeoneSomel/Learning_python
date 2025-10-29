numtotalpecas = int(input("Digite o número total de peças: "))
tolerancia = 0.5
tamideal = 15.0
soma_dos_tamanhos = 0.0
pecas_fora_tolerancia = 0
numtotalpecasf = numtotalpecas + 1
for x in range(1, numtotalpecasf):
    x = float(input(f"Digite o tamanho da {x}° peça (em cm): "))
    soma_dos_tamanhos = soma_dos_tamanhos + x
    desvio = abs(x - tamideal)
    if desvio > tolerancia:
        pecas_fora_tolerancia = pecas_fora_tolerancia + 1
media_tamanho = soma_dos_tamanhos / numtotalpecas
if pecas_fora_tolerancia == 0:
    print("Lote Aprovado: Qualidade Perfeita (0 peças fora da tolerância).")
elif pecas_fora_tolerancia >= 2:
    print("Lote Aceitável: Pequena correção necessária.")
else:
    print("Lote Reprovado: Alta taxa de defeito")
print(f"A média dos tamanhos das peças é {media_tamanho} cm e a quantidade de peças fora da tolerância é {pecas_fora_tolerancia}")
