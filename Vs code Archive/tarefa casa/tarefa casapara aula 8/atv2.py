temfinal = float(input("Qual o tempo final do atleta: "))
pen = input("O atleta recebeu alguma penalidade?(Sim ou não): ").lower()
clas = input("Qual a classificação da equipe?(Ouro, prata ou bronze?): ").lower()

if temfinal < 10 and pen == "não":
    print("Desempenho excelente: novo recorde pessoal.")
elif temfinal < 12 or clas == "ouro":
    print("Desempenho forte: classificado para a próxima fase.")
elif temfinal >= 12 and pen == "não":
    print("Desempenho regular: precisa de mais treinamento.")
else:
    print("Desempenho insuficiente: desclassificado.")
