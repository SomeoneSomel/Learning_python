avarage = float(input("A Média academica do aluno: "))
habwr = int(input("Habilidade escrita do aluno de 1 a 5: "))
fin = input("Ele tem dificuldades financeiras?(Sim ou não): ").lower()

print("")
if avarage >= 9 and habwr >= 4 :
    print("Parabéns! Você é elegível para a bolsa de mérito acadêmico.")
elif avarage >= 8 and fin == "sim":
    print("Parabéns! Você é elegível para a bolsa de necessidade financeira.")
elif avarage >= 7 and habwr >= 3 and fin == "sim":
    print("Parabéns! Você é elegível para a bolsa combinada de mérito e necessidade.")
elif avarage >= 7 and habwr >= 3:
    print("Você é elegível para a bolsa de necessidade, mas sua média e habilidade em escrita são requisitos")
else:
    print("Infelizmente, você não atende aos critérios de elegibilidade para bolsa")