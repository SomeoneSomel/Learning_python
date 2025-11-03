from tkinter import E


qnt = int(input("A quantidade de questões: "))
pontuacao_bruta = 0
erros_consecutivos = 0
qnt = qnt + 1
for x in range(1, qnt):
    x = float(input(f"A nota obtida na questão {x}: "))
    if x == 10:
        pontuacao_bruta = pontuacao_bruta + x
        erros_consecutivos = 0
    elif x < 5:
        pontuacao_bruta = pontuacao_bruta + x
        erros_consecutivos = erros_consecutivos + 1
    else:
        pontuacao_bruta = pontuacao_bruta + x
        erros_consecutivos = 0
if pontuacao_bruta > 40 and erros_consecutivos == 0:
    print("Resultado Excelente! Bônus de 10% aplicado.")
    pontuacao_ajustada = pontuacao_bruta * 1.10
elif pontuacao_bruta < 20 or erros_consecutivos > 2:
    print("Resultado Fraco. Penalidade de 15% aplicada")
    pontuacao_ajustada = pontuacao_bruta * 0.85
else:
    print("Resultado Padrão. Sem bônus ou penalidade")
    pontuacao_ajustada = pontuacao_bruta
print(f"A pontuação bruta foi de {pontuacao_bruta} e com o ajusta das penalidades/bonus é de {pontuacao_ajustada}")