lista = []
tamanho = input('qual o tamanho da lista? ')
tamanho = int(tamanho)

for index in range(tamanho):
    item = input('digite item ' + str(index) + ': ')
    item = int(item)
    lista.append(item)

print('antes de ordenar')
print(lista)
lista.sort()
print('depois de ordenar')
print(lista)
