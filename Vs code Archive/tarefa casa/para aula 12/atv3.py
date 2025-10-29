numproduto = int(input("A quantidade de produtos diferentes: "))
valor_total_estoque = 0
produtos_alto_risco = 0
numprodutof = numproduto + 1
for x in range(1, numprodutof):
    vlr = float(input(f"Digite o valor do {x}° produto: "))
    qntstock = int(input(f"Digite a quantidade em estoque do {x}° produto: "))
    valor_bruto = vlr * qntstock
    if qntstock > 100:
        valor_total_estoque = valor_total_estoque + (valor_bruto * 1.05)
    elif vlr > 50 and qntstock <= 10:
        produtos_alto_risco = produtos_alto_risco + 1
        valor_total_estoque = valor_total_estoque + valor_bruto
    else:
        valor_total_estoque = valor_total_estoque + valor_bruto
print(f"O valor final do estoque é R$ {valor_total_estoque} e a quantidade de produtos classificados como de alto risco é {produtos_alto_risco}")