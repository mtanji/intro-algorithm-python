notas = []
tamanho = input('qual o tamanho da lista de notas? ')
tamanho = int(tamanho)

for index in range(tamanho):
    item = input('digite nota ' + str(index + 1) + ': ')
    item = int(item)
    notas.append(item)

print(notas)

soma = 0
for nota in notas:
    soma += nota

media = soma / tamanho
print('média:', media)
