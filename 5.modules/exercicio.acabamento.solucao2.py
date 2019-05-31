acabamentos = ['médio padrão', 'alto padrão'] # variável global
ofertas = [170000, 200000]              # variável global
custoAcabamentoPorMetro = [430, 880]    # variável global
metragem = 78                           # variável global
custoAcabamentoTotal = []               # variável global

def calculaPrecoAcabamento():
    for index, custoPorMetro in enumerate(custoAcabamentoPorMetro):
        # variável local: custoTotal
        custoTotal = custoPorMetro * metragem
        custoAcabamentoTotal.append(custoTotal)
        print('custo acabamento', acabamentos[index], custoTotal)

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
    
