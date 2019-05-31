# Faça um programa, derivado deste anterior, para receber a quantidade de usuários para os quais ele deve calcular a média e indicar aprovação ou reprovação e então calcular a média de cada um deles.

quantidade = input('deseja calcular quantas médias? ')
quantidade = int(quantidade)

for rep in range(quantidade):
    nota1 = input('digite sua primeira nota ')
    nota1 = float(nota1)
    nota2 = input('digite sua segunda nota ')
    nota2 = float(nota2)
    media = (nota1 + nota2) / 2

    if media >= 6:
        print('media', media,': aprovado')
    else:
        print('media', media,': reprovado')
