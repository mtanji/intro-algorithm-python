valor = 10  # variável global
lado1 = 2   # variável global
lado2 = 5   # variável global
preco = 80.0  # variável global
desconto = 10 # variável global

# declaração do procedimento dobro
def dobro():
    # variável local: conta
    conta = valor * 2
    print('dobro:', conta)

# declaração do procedimento triplo
def triplo():
    # variável local: conta
    conta = valor * 3
    print('triplo:', conta)

# declaração do procedimento raiz_quadrada
def raiz_quadrada():
    # variável local: conta
    conta = valor ** 0.5
    print('raiz quadrada:', conta)

# declaração do procedimento area_retangulo
def area_retangulo():
    # variável local: area
    area = lado1 * lado2
    print('lado1:', lado1)
    print('lado2:', lado2)
    print('area retangulo:', area)

# declaração do procedimento calcula_desconto
def calcula_desconto():
    # variável local: precoDescontado
    precoDescontado = preco - preco * (desconto/100)
    print('preco:', preco)
    print('desconto:', desconto, '%')
    print('preco com desconto:', precoDescontado)



print('valor:', valor)

# ativação do procedimento dobro
dobro()

# ativação do procedimento triplo
triplo()

# ativação do procedimento raz_quadrada
raiz_quadrada()

# ativação do procedimento area_retangulo
area_retangulo()

# ativação do procedimento calcula_desconto
calcula_desconto()
