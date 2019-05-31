#def calc_media():
    # o que acontece se não inicializarmos as variáveis locais?
    # n1
    # n2
    # media = n1 + n2
    # print(media)

def calc_media2():
    # o que acontece se apenas referenciarmos as variáveis globais já inicializadas?
    nota1 = 2
    nota2 = 3
    media = (nota1 + nota2)/2
    print(media)

calc_media2()

# o que acontece se não inicializarmos as variáveis?
nota1 = 5
nota2 = 6
media = (nota1 + nota2)/2
print(media)

#calc_media()
calc_media2()

print('nota1:', nota1)
print('nota2:', nota2)

# quem define escopo? Em Python, if não define escopo, diferente de C

print('--- escopo função ---')
a=1
def func():
    a=2
    print('a in func\t',a)
print('a before func\t', a)
func()
print('a after func\t', a)

print('--- escopo if ---')
b=1
print('b before if\t',b)
if a == 1:
    b = 2
    print('b in if\t\t', b)
print('b after if\t',b)

def calc_media(N1, N2):
    print('N1:', N1)
    print('N2:', N2)
    media = (N1 + N2)/2
    print('media:', media)

calc_media(5, 6)
calc_media(7, 8)

def calc_media(N1, N2, turma):
    print('N1:', N1)
    print('N2:', N2)
    print('turma:', turma)
    media = (N1 + N2)/2
    print('m:', media, ' t:', turma)

calc_media(5, 6, 'SI')
calc_media(7, 8, 'Redes')
#calc_media('Redes', 7, 8)


def f_calc_media(N1, N2):
    print('N1:', N1)
    print('N2:', N2)
    media = (N1 + N2)/2
    return media

media = f_calc_media(4, 5)
print('media:', media)
media = f_calc_media(9, 10)
print('media:', media)

