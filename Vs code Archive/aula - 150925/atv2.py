#---------------------------------/
# EXPLIQUE O QUE FAZ ESSE PROGRAMA/
#                                 /
# EXPLIQUE OS IF/ELSE ANINHADOS   /
#---------------------------------/
peso = float(input("Digite o peso do pacote em kg: ")) #pede o peso para o usuario inserir
destino = input("Digite o destino ('local' ou 'nacional'): ").lower() #pede o destino para o usuario inserir e força para ser minusculo

custo_total = 0.0 #define o custo para '0'

if destino == 'local': #se for local, executa esse codigo:
    custo_base = 5.00#define custo base para 5
    if peso > 10:#se peso for maior que dez, ele vai...
        excesso_peso = peso - 10 #vai calcular o peso em excesso.
        custo_extra = excesso_peso * 2.00 #calcular o custo extra do processo
        custo_total = custo_base + custo_extra #e vai calcular qual vai ser o preço total.
    else:#caso o peso não for maior que 10, ele vai...
        custo_total = custo_base #não realiza nenhuma conta, só vai mostrar o preço.
    print(f"O custo total do envio para o destino local é: R$ {custo_total:.2f}") #aqui, ele mostra o preço para o usuario.

else:  #caso não seja local , ele executará esse codigo.
    if destino == 'nacional': #se for nacional...
        custo_base = 15.00#ele definirá custo base para 15
        if peso > 10: #se peso for maior que dez, ele vai...
            excesso_peso = peso - 10 #vai calcular o peso em excesso
            custo_extra = excesso_peso * 5.00 #calcular o custo extra do processo
            custo_total = custo_base + custo_extra #e vai calcular qual vai ser o preço total.
        else:# caso não for maior que 10...
            custo_total = custo_base #simplismente mostrará o custo base sendo o custo total.
        print(f"O custo total do envio para o destino nacional é: R$ {custo_total:.2f}")  #aqui, ele mostra o preço para o usuario.
    else: #caso não for nem local, nem nacional.
        print("Erro: Destino inválido. Por favor, digite 'local' ou 'nacional'.") #mostrará que deu um erro e avisará para o usuario que ele deve digitar local ou nacional.