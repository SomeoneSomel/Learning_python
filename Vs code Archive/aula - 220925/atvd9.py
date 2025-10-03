tp = input("Tipo do plano(Básico, Padrão ou Premium): ").lower()
temp = int(input("Tempo da assinatura em meses: "))
part = input("A conta é compartilhada: ").lower()

if tp == "premium" and temp >= 24:
    print("Você é um cliente premium de longa data: 25% de desconto vitalício!")
elif tp == "padrão" and temp > 12 and part == "não":
    print("Você atende aos critérios para um desconto de 15%.")
elif tp == "básico" and temp > 6:
    print("Sua lealdade merece um reconhecimento: 5% de desconto na próxima fatura.")
else:
    print("Nenhum desconto disponível no momento para o seu perfil.")