#isso é para definir o tamanho do vetor, sendo ele 5
TAMANHO_VETOR = 5
# será usado depois, então será alocado na memoria agora
vetor_notas = [0.0] * TAMANHO_VETOR
soma_notas = 0.0  # acumulador
media = 0.0       # a variavel do calculo final
print("--- Entrada de 5 Notas ---")
#laço for, que será solicitado a nota a quantidade de tamanho do vetor(5) e atribui a nota no vetor.
for i in range(TAMANHO_VETOR):
    # isso é para solicitar a nota, com um {i + 1} só para deixar o texto bonitinho.
    nota = float(input(f"Digite a Nota {i + 1} (Posição [{i}]): "))
    # isso é para atribuir a nota no indice
    vetor_notas[i] = nota
print("\n--- Processamento dos Dados ---")
# é usado o indice i para ter certeza que irá percorrer as 5 vezes
for i in range(TAMANHO_VETOR):
    # agora somamos as notas usando o indice i para pegar as notas do vetor
    soma_notas = soma_notas + vetor_notas[i]
# um if para fazer a média, garantindo que seja maior que zero só para garantir que não vai ter divisão de zero
if TAMANHO_VETOR > 0:
    media = soma_notas / TAMANHO_VETOR
# e aqui é printado os resultados.
print(f"Vetor de Notas Registrado: {vetor_notas}")
print(f"Soma Total das Notas: {soma_notas:.2f}")
print(f"Média Final da Turma: {media:.2f}")