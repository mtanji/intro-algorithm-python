frente = [5, 6, 7]              # variável global
profundidade = [30, 28, 23]     # variável global
preco = [50000, 53000, 52000]   # variável global

def calculaPrecoPorMetro():
    custoPorMetroQuadrado = []  # variável local
    for i in range(3):
        custo = preco[i] / (frente[i] * profundidade[i]) # variável local: custo
        custoPorMetroQuadrado.append(custo)
        print('terreno', i, custo)

    menorCusto = 100000         # variável local
    for custo in custoPorMetroQuadrado:
        if (custo < menorCusto):
            menorCusto = custo
    print(menorCusto)

calculaPrecoPorMetro()
