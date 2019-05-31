# [Parte 1] Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.

nota1 = input('digite sua primeira nota ')
nota1 = float(nota1)
nota2 = input('digite sua segunda nota ')
nota2 = float(nota2)
media = (nota1 + nota2) / 2

if media >= 6:
    print('media', media,': aprovado')
else:
    print('media', media,': reprovado')
