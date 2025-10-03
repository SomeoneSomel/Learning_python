print("Igor freitas da silva - 0220482523011 - sei lá, pão.")
#Igor freitas da silva - 0220482523011 - sei lá, pão.

r_investimento = float(input("O retorno no investimento(em decimal): "))
r_livre = float(input("A taxa livre de riscos(em decimal): "))
sigma = float(input("O desvio-padrão da volatilidade(em decimal): "))

if sigma == 0:
    print("Erro! O valor de sigma é zero, a operação foi cancelada para evitar divisão por zero.")
    sharp = 0
else:
    sharp = (r_investimento - r_livre) / sigma
spread = r_investimento - r_livre

if sharp > 1.5 and spread > 0.05:
    print("Investimento Excelente: Alta performance ajustada ao risco")
    clas = "Excelente"
elif sharp > 0.5 and sharp < 1.5 or spread > 0.02:
    print("Investimento Bom: Risco e retorno moderados")
    clas = "Boa"
elif sharp < 0.5 and r_investimento > 0:
    print("Investimento Aceitável: Retorno positivo, mas risco alto para o ganho.")
    clas = "Aceitável"
else:
    print("Investimento Ruim: Não recomendado.")
    clas = "Ruim"

print(f"O valor de Sharp foi {sharp} e a classificação foi {clas}")