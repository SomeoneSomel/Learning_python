qta = int(input("Quantidade de alunos na sala: "))
smnotas = 0

for i in range(qta):
    i = int(input("Nota do aluno: "))
    smnotas = smnotas + i
print(f"A soma das notas é {smnotas}")