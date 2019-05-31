# As temperaturas nos Estados Unidos são medidas em graus Fahrenheit, por isso você não sabe se está fazendo frio ou calor em Chicago. Para resolver isso, escreva um programa que receba a temperatura em graus Fahrenheit e imprima a temperatura em graus Celsius. A fórmula de cálculo é 
#		grausCelsius = ( grausFahrenheit - 32 ) * (5/9).
# Em seguida, se a temperatura estiver maior que 30 graus Celsius, imprima “Está fazendo calor”, se a temperatura estiver menor que 20 graus Celsius, imprima “Está fazendo frio”, e se a temperatura estiver em uma faixa fora das anteriores, imprima “Está fazendo um clima ameno”.


fahrenheit = input('qual a temperatura em fahrenheit? ')
fahrenheit = float(fahrenheit)

celsius = (fahrenheit - 32) * (5/9)

if celsius > 30:
    print('está fazendo calor')
elif celsius < 20:
    print('está fazendo frio')
else:
    print('está fazendo um clima ameno')
