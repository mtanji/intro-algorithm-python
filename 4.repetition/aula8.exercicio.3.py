# Escreva um programa que ordene uma lista numérica. Primeiramente, o programa deve pedir o tamanho da lista. Depois, o programa deve pedir que o usuário digite os números de acordo com o tamanho da lista. Então, o programa deve usar o método de ordenação de lista, list.sort(). Por fim, o programa deve iterar pela lista e imprimir a lista item a item.

tamanho = input('deseja inserir quantos números na lista? ')
tamanho = int(tamanho)
lista = []

for rep in range(tamanho):
    num = input('digite um número para a lista ')
    num = float(num)
    lista.append(num)

lista.sort()

for item in lista:
    print(item)
