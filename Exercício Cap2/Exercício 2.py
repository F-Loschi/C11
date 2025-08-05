tabuada = int(input('Vai querer a tabuada de qual número? '))
inicio = int(input('Vai começar onde? '))
fim = int(input('E vai terminar onde? '))

for i in range(inicio,fim+1):
    print(i*tabuada)