lista_notas = []
NUMERO_NOTAS = 5
for i in range(NUMERO_NOTAS):
    i = float(input(f"Qual a nota do {i + 1}° aluno: "))
    lista_notas.append(i)

for i in range(len(lista_notas)):
    atual = lista_notas[i]
    print(f"A nota na posição {i + 1} é a {atual}")
