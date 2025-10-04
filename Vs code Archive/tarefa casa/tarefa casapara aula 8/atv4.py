p = float(input("Valor do emprestimo: "))
ja = float(input("Taxa de juros anual: "))
n = int(input("Prazo de emprestimo em meses: "))

jm = (ja / 12) / 100
pgm = p * (jm * (1 + jm)**n) / ((1 + jm)**n - 1)
if pgm < 200:
    print("Pagamento mensal baixo")
elif pgm >= 200 and pgm <= 500:
    print("Pagamento mensal moderado")
elif pgm > 500:
    print("Pagamento mensal alto")