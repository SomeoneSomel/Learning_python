v_inicial = float(input("Valor inicial do investimento: "))
nummes = int(input("Quantidade de meses: "))
valor_acumulado = 0.0
juros_totais = 0.0
nummesfor = nummes + 1
for x in range(1, nummesfor):
     taxa = float(input(f"Digite a taxa de crescimento do mês: "))
     if taxa > 0.015:
        juros = valor_acumulado * taxa
     elif 0.005 <= taxa <= 0.015:
        juros = valor_acumulado * taxa * 0.9
     else:
        juros = 0.0
     valor_acumulado = valor_acumulado + juros
     juros_totais = juros_totais + juros
if juros_totais > (v_inicial * 0.10):
    print("Investimento de Alto Sucesso! (Retorno superior a 10%)")
else:
    print("Investimento Moderado. Retorno abaixo do esperado.")