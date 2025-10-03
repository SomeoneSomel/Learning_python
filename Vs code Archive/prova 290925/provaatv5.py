print("Igor freitas da silva - 0220482523011 - sei lá, pão.")
#Igor freitas da silva - 0220482523011 - sei lá, pão.

c_inicial = float(input("O custo: "))
q = float(input("A quantidade: "))
dias = int(input("Os dias em atraso: "))
defeito = float(input("A porcentagem de defeitos(em decimal): "))

if c_inicial > 5000 and q > 1000:
    f_comp = 1.15
else:
    f_comp = 1.05
c_corrigido = c_inicial * f_comp

if defeito > 0.10 or dias > 5:
    print("Penalidade Alta: 20% de redução no lucro")
    c_final = c_corrigido * 1.25
elif defeito > 0.05 and defeito < 0.10 and dias > 0:
    print("Penalidade Média: 10% de redução no lucro")
    c_final = c_corrigido * 1.10
else:
    print("Sem penalidade. Custo final apenas com correção.")
    c_final = c_corrigido

print(f"O custo base foi de R${c_corrigido}. O valor final com os descontos/acrescimos foi de R${c_final}")