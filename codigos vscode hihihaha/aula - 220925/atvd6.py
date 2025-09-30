exp =  int(input("Tempo de experiencia em vendas em anos: "))
habcom = int(input("Habilidade de comunicação avaliada de 1 a 10: "))
disp = input("Disponibilidade(Integral ou Meio-período): ").lower()

print("")
if exp > 2 and habcom > 8:
    print("Candidato classificado como Sênior. Entra na próxima etapa para vaga integral.")
elif exp > 2 and habcom > 6:
    print("Candidato classificado como Sênior. Entra na próxima etapa para vaga de meio período")
elif exp > 1 and habcom > 8 and disp == "meio-período":
    print("Candidato classificado como Pleno. Entra na próxima etapa para vaga de meio período")
elif exp > 1 and habcom > 8 and disp == "integral":
    print("Candidato classificado como Pleno. Entra na próxima etapa para vaga integral.")
elif habcom > 7 and disp == "meio-período":
    print("Candidato classificado como Júnior. Entra na próxima etapa para vaga de meio período")
elif habcom > 7 and disp == "integral":
    print("Candidato classificado como Júnior. Entra na próxima etapa para vaga integral")
else:
    print("Candidato não classificado. Não atende aos requisitos mínimos.")
