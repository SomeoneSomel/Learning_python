print("Igor Freitas da Silva - 0220482523011 - sei la, pão")
nomes = []
rendas = []
status_aprovacao = []
while nomes != "fim":
    nome = input("Insira o nome do cliente (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    renda = float(input("Insira a renda mensal do cliente: R$"))
    nomes.append(nome)
    rendas.append(renda)
    if renda > 2500:
        status_aprovacao.append("Aprovado")
    else:
        status_aprovacao.append("Reprovado")
cont_aprovados = 0
media_renda = 0
somamedia = 0
for i in range(len(nomes)):
    if status_aprovacao[i] == "Aprovado":
        cont_aprovados += 1 
        somamedia += rendas[i]
media_renda = somamedia / cont_aprovados
print(f"Clientes: {nomes}, Status: {status_aprovacao}, Média de renda dos aprovados: R${media_renda}")