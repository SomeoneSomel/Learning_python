V_base = float(input("Digite o valor do bonus: "))
P_ind = int(input("Digite a pontuação individual(0 a 100): "))
P_equipe = int(input("Digite a pontuação da equipe(0 a 100): "))
if P_ind > 90:
    fap = 1.25
elif P_ind > 70:
    fap = 1.10
elif P_ind > 50:
    fap = 1.0
else:
    fap = 0.8
B_ajustado = V_base * fap
if P_equipe > 85:
    if P_ind > 95 or B_ajustado > 5000:
        print("Bônus Máximo (30% Extra)")
        B_final = B_ajustado * 1.30
    else:
        print("Bônus Padrão (10% Extra)")
        B_final = B_ajustado * 1.10
elif P_equipe >= 60 and P_equipe <= 85:
    if P_ind < 60:
        print("Penalidade por Desempenho Individual (15% de Redução)")
        B_final = B_ajustado * 0.85
    else:
        print("Sem Alteração Adicional")
        B_final = B_ajustado
else:
    print("Penalidade Severa (25% de Redução)")
    B_final = B_ajustado * 0.75
print(f"O Valor base do bônus é: R$ {V_base}, o fator de ajuste aplicado foi {fap} e o valor final do bônus é: R$ {B_final}")