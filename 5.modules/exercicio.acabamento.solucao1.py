ofertas = [170000, 200000]              # variável global
custoAcabamentoPorMetro = [430, 880]    # variável global
metragem = 78                           # variável global
custoAcabamentoTotal = []               # variável global

def calculaPrecoAcabamento():
    for i in range(len(ofertas)):
        # variável local: custoTotal
        custoTotal = custoAcabamentoPorMetro[i] * metragem
        custoAcabamentoTotal.append(custoTotal)
        print('acabamento', i, custoTotal)

calculaPrecoAcabamento()

indiceAltoPadrao = 1                    # variável global
indiceMedioPadrao = 0                   # variável global
diferencaOferta = ofertas[indiceAltoPadrao] - ofertas[indiceMedioPadrao]
diferencaCustos = custoAcabamentoTotal[indiceAltoPadrao] - custoAcabamentoTotal[indiceMedioPadrao]

print('diferença entre ofertas:', diferencaOferta)
print('diferença entre custos:', diferencaCustos)

if (diferencaCustos > diferencaOferta):
    print('venda para quem ofertou 170.000')
else:
    print('venda para quem ofertou 200.000')
    
