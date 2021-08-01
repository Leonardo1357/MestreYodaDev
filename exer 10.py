numero = float(input('Digite um valor para saber a sua tabuada: '))

def tabuada(numero):
    i = 0
    while (i < 15):
        print(f'{numero} * {i} = {numero * i}')
        i += 1;

tabuada(numero)
