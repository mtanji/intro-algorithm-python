notas1SI = []
notas2SI = []
notas1CCO = []
notas2CCO = []
mediasSI = []
mediasCCO = []

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


def calcularMedias(vetorNotas1, vetorNotas2, vetorMedias):
    for i in range(len(vetorNotas1)):
        media = (vetorNotas1[i] + vetorNotas2[i]) / 2
        vetorMedias.append(media)

def imprimirMedias(vetorMedias):
    for i in vetorMedias:
        print(i)

lerNotas()
calcularMedias(notas1SI, notas2SI, mediasSI)
calcularMedias(notas1CCO, notas2CCO, mediasCCO)
imprimirMedias(mediasSI)
imprimirMedias(mediasCCO)




