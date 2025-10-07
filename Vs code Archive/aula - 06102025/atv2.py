numtab = int(input("Digite o número inteiro para ver a tabuada: "))

print(f"Tabuada do {numtab}")

for i in range(1, 11):
  r = numtab * i
  print(f"{numtab} x {i} = {r}")
