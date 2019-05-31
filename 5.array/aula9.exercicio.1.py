# Você vai viajar para Chicago e precisa saber quantos dólares vai poder levar. Para resolver isso, escreva um programa que receba uma quantidade em reais e a cotação do dólar. Se a quantidade de dólares que consegue comprar for maior que US$5.000, imprima “Você está rico”, se a quantidade de dólares for menor que US$50, imprima “Você está pobre”, e se a quantidade não corresponder aos intervalos anteriores, imprima “Você não está rico e nem está pobre”.

reais = input('quantos reais voê tem para levar? ')
reais = float(reais)

cotacao = input('qual a cotação do dólar? ')
cotacao = float(cotacao)

dolares = reais / cotacao
if dolares > 5000:
    print('você está rico! \o/')
elif dolares < 50:
    print('você está pobre... :(')
else:
    print('você não está rico e nem está pobre')
    
