# Pois bem, acontece que brasileiro é insistente e não desiste nunca. Você não vai sair da loja de mãos abanando se faltar dinheiro. Nesse caso, você vai escolher itens da sua cesta e ir tirando um a um até fazer o valor da compra caber no orçamento. Para resolver isso, escreva um programa que use uma estrutura de dados linear e homogênea para armazenar os preços de cada item que está no carrinho. Use essa estrutura para armazenar os preços conforme eles são inseridos nele, de acordo com o indicado no programa anterior. Ou seja, você vai modificar o programa do exercício anterior. Assim, quando o valor da compra superar a quantidade de dinheiro que você tem, depois de imprimir “Não foi desta vez, tire alguns itens da cesta”, imprima a lista de preços dos itens que você tem na sua cesta e então pergunte pelo item que deseja remover. A escolha do item a ser removido pode ser feita de duas maneiras, pelo índice da lista ou pelo valor do preço. Escolha uma das formas e então faça o programa receber a informação necessária, remova o item da lista e então verifique novamente o valor total da sua compra. Se o novo valor total couber no orçamento, imprima “Boas compras e bom retorno” e encerre o programa, senão continue pedindo para retirar mais itens, até que a compra caiba no orçamento.

imposto = input('qual o valor do imposto (em %)? ')
imposto = float(imposto)

quantidade = input('quantos produtos comprou? ')
quantidade = int(quantidade)

compras = []
total = 0
for idx in range(quantidade):
    valor = input('digite o valor do produto ' + str(idx + 1) + ': ')
    valor = float(valor)
    total += valor
    compras.append(valor)

na_carteira = input('quanto você tem na carteira? ')
na_carteira = float(na_carteira)

total_com_imposto = total * (1 + imposto / 100)

print(total_com_imposto)

while na_carteira < total_com_imposto:
    print('não foi desta vez, tire alguns itens da cesta')
    print(compras)
    indice = input('selecione o indice de um item para retirar: ')
    indice = int(indice)
    valor = compras.pop(indice)
    total_com_imposto -= valor * (1 + imposto / 100)

print('boas compras e bom retorno')
