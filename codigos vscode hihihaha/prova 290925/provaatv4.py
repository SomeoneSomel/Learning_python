print("Igor freitas da silva - 0220482523011 - sei lá, pão.")
#Igor freitas da silva - 0220482523011 - sei lá, pão.

P = float(input("O valor inicial do investimento: "))
T = int(input("O tempo de investimento em meses: "))

if T < 6:
    J = 0.005
elif T > 6 and T < 12:
    J = 0.008
elif T >= 12:
    J = 0.012

rt = P * J * T
print(f"Por ter aplicado {T} meses em investimentos, você terá uma taxa de {J} ao mes, o que irá gerar R${rt} em juros!")