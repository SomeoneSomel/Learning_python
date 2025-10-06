#o comando for é o comando do python usado para repetir ações, sequencias ou palavras, o que for dado a ele e qual maneiira
# ele irá repetir dependendo da variavel depois do "in". alé mde que é necesssário criar uma variavel temporaría
#que no meu caso é a variavel "x".
print("Digite três palavras e elas serão repetidas em sequência")
print("===============================================")

#aqui estou pedindo para o usuário digitar três palavras e armazenando elas em variaveis
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
palavra3 = input("Digite a terceira palavra: ")
#depois disso, armazeno elas numa variavel chamada "repetir", usando virgula para deixar elas em sequencia
# e para funcionar o for do jeito que quero(descobri isso enquanto eu pesquisava o for, foi bem legal)
repetir = (palavra1, palavra2, palavra3)

#aqui é o for, que vai repetir as palavras em sequencia, uma por vez, e as palavras que serão repetidas
# dependem do que o usuário digitou, resumidamente:
for x in repetir: #aqui a variavel temporaria "x" vai receber cada palavra da variavel "repetir", uma por vez
    print(x) #aqui o comando print vai printar a variavel "x" usando o que recebeu do "repetir"  
#é bem simples, mas é dá pra entender, né?
# porem tem outros jeitos de fazer isso, tipo um que que pega uma palavra que separa cada letra, e printa cada letra
