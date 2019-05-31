custoUnitario = [0.35, 0.45]    # variável global
unidadesPorMetro = [37, 30]     # variável global
custoMateriaisPorMetro = [9, 7] # variável global
metragemParedes = 200           # variável global

def calculaPrecoConstrucao():
    custosTotais = []  # variável local
    for i in range(len(custoUnitario)):
        # variáveis locais: custoTijolos, custoTotalPorMetro e custoTotal
        custoTijolos = custoUnitario[i] * unidadesPorMetro[i]
        custoTotalPorMetro = custoTijolos + custoMateriaisPorMetro[i]
        custoTotal = custoTotalPorMetro * metragemParedes
        custosTotais.append(custoTotal)
        print('método', i, custoTotal)

    menorCusto = 100000         # variável local
    for custo in custosTotais:
        if (custo < menorCusto):
            menorCusto = custo
    print('menor custo:', menorCusto)

calculaPrecoConstrucao()
