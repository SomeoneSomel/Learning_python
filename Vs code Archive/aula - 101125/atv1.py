#isso vai criar uma lista com varias variaveis, como uma sacola cheia de frutas, com as frutas sendo as variaveis.
lista_frutas = ["Maçã", "Banana", "Uva", "Pêra", "Manga"]
print("--- Análise da Lista ---")
#isso só vai printar na tela as variaveis na lista, já que lista_frutas é a variavel lista com as variaveis dentro. 
print("Lista completa:", lista_frutas)
#a variavel primeiro vai acessar a lista "lista_frutas" para coletar o valor 0, que é a primeira variavel da lista(que é maçâ), e apos isso printar essa primeira variavel.
primeiro = lista_frutas[0]
print("1. Primeiro elemento (índice 0):", primeiro)
#o mesmo do de cima, porém com a terceira variavel da lista.
terceiro = lista_frutas[2]
print("2. Terceiro elemento (índice 2):", terceiro)
#novamente, porém com a ultima variavel, usando
ultimo = lista_frutas[-1]
print("3. Último elemento (índice -1):", ultimo)