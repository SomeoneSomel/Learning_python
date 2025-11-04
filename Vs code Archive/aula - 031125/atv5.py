# o programa escolhe um numero aleatorio usando a função random importada da biblioteca python, com ela, usa o while para perguntar para o usuario
# um numero que ele acha que é o correto, e faz isso até ele acertar, usando ifs para determinar a resposta se é correta ou errada.

import random

numero_secreto = random.randint(1, 6) 
tentativas = 0
acertou = False
palpite_usuario = 0 

while not acertou:
     palpite_usuario = int(input("Seu palpite: "))
     if palpite_usuario < 1 or palpite_usuario > 6:
        print("Palpite fora do intervalo. Tente um número entre 1 e 6.")
        continue
    
     tentativas += 1
    
     if palpite_usuario == numero_secreto:
        acertou = True # Altera a variável de controle para sair do loop
        print("\n*** Parabéns! Você acertou! ***")
    
     else:
        # Dica simples para manter o jogo ativo
        print("Errado. Tente novamente.")

print(f"O número sorteado era: {numero_secreto}")
print(f"Você precisou de {tentativas} tentativa(s) para acertar.")