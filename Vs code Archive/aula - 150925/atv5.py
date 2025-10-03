rmen = float(input("Digite a renda mensal: "))
score = int(input("Digite seu score: "))
tta = int(input("Digite o tempo trabalhado em anos: "))

if rmen > 3000 and tta >= 2:
    if score >= 700 and score <= 1000:
        print("Empréstimo aprovado com taxa de juros baixa!")
    else:
        print("Score de crédito insuficiente.")
else:
    print("Não elegível: Renda ou tempo de trabalho insuficientes")