from operator import index


cidades = []
NUMERO_CIDADES = 5
for x in range(NUMERO_CIDADES):
    x = input(f"Digite o nome da cidade {x + 1}: ")
    cidades.append(x)

for i in range(len(cidades)):
    cdm = cidades[i].upper()
    print(f"Cidade {i + 1}: {cdm}")

