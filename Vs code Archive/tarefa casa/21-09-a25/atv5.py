# o comenado if/elif/else são os comando de "e se?" do python. no caso do elif
# ele é como se fosse um "se não for isso, tente aquilo."

# nesse exemplo, estou fanzedo como seria um sistema de sinal de transito e sua
# "legenda" entre aspas ou o que signifca. sei lá não sou muito criativo.

#isso está pedindo a cor do sinal. é possivel por "vermelho", "amarelo" e "verde"
est = input("Vermelho, Amarelo ou Verde?: ").lower()

# aqui começa o if statement, onde ele verifica se está foi inserido "vermelho"
if est == "vermelho":
    print("Sinal Fechado, pare!") #se colocou, ele printa isso
# senão, ele verifica se foi inserido "amarelo"
elif est == "amarelo":
    print("Sinal de Atenção, prepare-se para parar!") #se sim, ele printa isso
# se não, é assumido que é verde
else:
    print("Sinal Aberto, pode passar!") #E logo printa isso.

# é um método mais facil do que colocar outro if statement no else, além de que pelas minhas pesqusias
# é possivel colocar mais de um, o que deixa mais versatil e util para varios tipos de programas