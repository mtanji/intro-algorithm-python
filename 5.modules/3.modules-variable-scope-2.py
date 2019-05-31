
varExterna = "Follow the Rabbit"

varExternaGrito = "PULL OVER THE CAR!!!"

def procedimento():
    print('begin procedimento')
    varInterna = 'This is Sparta!!!'
    varExterna = 'I know Kung-Fu'
    global varExternaGrito
    varExternaGrito = "EASY BOY!"
    print('varExterna\t', varExterna) # variável escopo interno, não sobrescreve variável de escopo externo
    print('varInterna\t', varInterna)
    print('end procedimento')


print('varExterna\t', varExterna) # variável escopo externo
print('varExternaGrito\t', varExternaGrito) # variável escopo externo
procedimento()
print('varExterna\t', varExterna) # variável escopo externo
print('varExternaGrito\t', varExternaGrito) # variável escopo externo
print('varIntena\t', varIntena)  # variável escopo interno, que não está mais acessível
