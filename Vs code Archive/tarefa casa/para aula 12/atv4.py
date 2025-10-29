numlancamentos = int(input("Digite o número de lançamentos: "))
saldo_final = 0.0
total_receitas = 0.0
total_despesas = 0.0
numlancamentosf = numlancamentos + 1
for x in range(1, numlancamentosf):
    x = float(input(f"Digite o valor do {x}° lançamento (positivo para receita e negativo para despesa): "))
    if x > 0:
        total_receitas = total_receitas + x
    else:
        total_despesas = total_despesas + x
    saldo_final = saldo_final + x
if saldo_final > 0 and total_receitas > total_despesas * 2:
    print("Situação Excelente: Bônus de 5% sobre o saldo aplicado")
    Saldo_Ajustado = saldo_final * 1.05
elif saldo_final > 0:
    print("Situação Boa: Sem bônus ou taxa.")
    Saldo_Ajustado = saldo_final
else:
    print("Situação Ruim: Taxa de serviço de 2% aplicada")
    Saldo_Ajustado = saldo_final * 0.98
print(f"O total de receitas é R$ {total_receitas}, o total de despesas é R$ {total_despesas} e o saldo final ajustado é R$ {Saldo_Ajustado}")
    