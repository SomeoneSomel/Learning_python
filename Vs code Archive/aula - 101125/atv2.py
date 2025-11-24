# aqui ele define o tamanho do vetor para 5
TAMANHO_VETOR = 5
#aqui é alocado o espaço da memoria, adcionando 5 strings vazias para uma lista
vetor_nomes = [""] * TAMANHO_VETOR
#Aqui é iniciado um loop for que vai pedir o nome para ser colocado na lista cinco vezes(o tamanho do vetor)
print("--- Entrada de Nomes (5 Posições Fixas) ---")
for i in range(TAMANHO_VETOR):
    nome = input(f"Digite o nome do Aluno {i + 1} (Posição [{i}]): ")
    vetor_nomes[i] = nome
print("\n--- Processamento dos Dados ---")
#aqui irá printar o nome dos vetores inseridos pelo usuario.
print("Os nomes registrados, acessados por índice:")
for i in range(TAMANHO_VETOR):
    nome_atual = vetor_nomes[i]
    print(vetor_nomes[i])