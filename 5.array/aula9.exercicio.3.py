# O imposto sobre o consumo nos Estados Unidos varia entre os estados e é calculado na hora do pagamento. Ou seja, se um produto está a US$10,00 na gôndola e o imposto for de 7%, o caixa passa o produto e te cobra os US$10,00 somados do imposto de 7%, ou seja, US$10,70. Acontece que antes de voltar para o Brasil, você passa no outlet, passa por uma loja e põe vários itens na sua cesta, mas não sabe se tem dinheiro suficiente para pagar a conta. Para resolver isso, escreva um programa que receba o valor do imposto (em %) no estado onde você está, a quantidade de produtos que você colocou na cesta, o valor de cada produto que foi colocado na cesta e a quantidade de dólares que sobrou na sua carteira depois de passear. O programa deve calcular o valor total da sua compra e imprimir o resultado, depois deve imprimir “Boas compras e bom retorno” se o dinheiro foi suficiente, ou imprimir “Não foi desta vez, tire alguns itens da cesta” se o dinheiro não foi suficiente para pagar o valor total da conta.

imposto = input('qual o valor do imposto (em %)? ')
imposto = float(imposto)

quantidade = input('quantos produtos comprou? ')
quantidade = int(quantidade)

total = 0
for idx in range(quantidade):
    valor = input('digite o valor do produto ' + str(idx + 1) + ': ')
    valor = float(valor)
    total += valor

na_carteira = input('quanto você tem na carteira? ')
na_carteira = float(na_carteira)

total_com_imposto = total * (1 + imposto / 100)

print(total_com_imposto)

if na_carteira >= total_com_imposto:
    print('boas compras e bom retorno')
else:
    print('não foi desta vez, tire alguns itens da cesta')
