i = int(input("Digite a idade do público: "))
gen = input("Gênero do filme(Terror ou ação): ").lower()

print("")
if i < 18 and gen == "terror":
    print("Este filme não é recomendado para sua idade devido ao gênero.")
elif i <16 and gen == "ação":
    print("Este filme de ação não é adequado para sua faixa etária.")
elif i >= 18 or gen == "ação":
    print("Recomendado para você assistir o filme.")
else:
    print("Não há recomendações para este filme ou idade.")
