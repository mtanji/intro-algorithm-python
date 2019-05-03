notas1SI = []
notas2SI = []
notas1CCO = []
notas2CCO = []
mediasSI = []
mediasCCO = []
#nota1 = 0
#nota2 = 0
#media = 0

def lerNotas():
    for i in range(3):
        nota1 = int(input('nota 1:'))
        notas1SI.append(nota1)
        nota2 = int(input('nota 2:'))
        notas2SI.append(nota2)
    for i in range(3):
        nota1 = int(input('nota 1:'))
        notas1CCO.append(nota1)
        nota2 = int(input('nota 2:'))
        notas2CCO.append(nota2)


def calcularMediasSI():
    for i in range(3):
        media = (notas1SI[i] + notas2SI[i]) / 2
        mediasSI.append(media)

def calcularMediasCCO():
    for i in range(0,3):
        media = (notas1CCO[i] + notas2CCO[i]) / 2
        mediasCCO.append(media)

def imprimirMedias():
    for i in mediasSI:
        print(i)
    for i in mediasCCO:
        print(i)

lerNotas()
calcularMediasSI()
calcularMediasCCO()
imprimirMedias()

