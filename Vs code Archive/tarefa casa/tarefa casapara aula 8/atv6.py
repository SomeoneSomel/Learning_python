P = float(input("Valor do emprestimo: "))
janual = float(input("Taxa de juros anual: "))
N = int(input("Prazo de emprestimo em meses: "))
jmensal = (janual / 12) / 100
pagamento = P * (jmensal * (1 + jmensal)**N) / ((1 + jmensal)**N - 1)
if pagamento < 200:
    print("Pagamento mensal baixo")
elif pagamento >= 200 and pagamento <= 500:
    print("Pagamento mensal moderado")
elif pagamento > 500:
    print("Pagamento mensal alto")