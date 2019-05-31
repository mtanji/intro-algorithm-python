def calcula(x, y, cond):
  if (cond):
    x[0] = 2018
    y = 12
    flag = 0
  return y

ano = [2000]
#ano.append(int(input("Digite o ano: ")))
#mes = int(input("Digite o mes: "))
mes=1
if (ano[0] > 2018):
  flag = 1
  mes = calcula(ano, mes, flag)
  print(f"{ano[0]}, {mes}, {flag}")

#===============
print('Estamos a {0:0.2f} anos-luz da Terra'.format(5.2384645))
#===============

def temperatura_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * (5 / 9)

fahrenheit = float(input('Qual a temperatura atual? '))
temperatura_celsius(fahrenheit)
print('Agora está fazendo', celsius, 'graus celsius.')

