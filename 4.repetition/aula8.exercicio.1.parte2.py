# [Parte 2] Faça um programa, derivado deste anterior, para receber a quantidade de usuários para os quais ele deve fazer a indicação de maioridade, então receber a idade e dizer se é maior ou menor de idade essa quantidade de vezes. Por exemplo, se o usuário digitar 3, deve pedir a idade da primeira pessoa e dizer se é maior de idade, então pedir a idade do segunda pessoa e dizer se é maior de idade, e assim sucessivamente até que a pergunta tenha sido respondida na quantidade de vezes em que o usuário indicou.

quantidade = input('querer saber a situação de quantos usuários? ')
quantidade = int(quantidade)

for rep in range(quantidade):
    idade = input('digite sua idade ')
    idade = int(idade)

    if idade >= 18:
        print('maior de idade')
    else:
        print('menor de idade')
