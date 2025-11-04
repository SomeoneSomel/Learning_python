senha_correta = "python123"
tentativas_erradas = 0
senha_digitada = ""

print("\n--- Sistema de Login ---")

while senha_digitada != senha_correta:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print(f"\nSenha válida! Acesso concedido.")
    else:
        tentativas_erradas += 1
        print("Senha incorreta. Tente novamente.")

print ("Total de entradas erradas", tentativas_erradas)

#RESPONDA: Porque a variável senha_digitada começa com vazio ""
# por que é preciso para fazer o while rodar pelo menos uma vez, caso não tenha, ele irá ser somente skipado.