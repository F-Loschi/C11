numero = int(input('Entre um número entre 1000 e 9999: '))
while numero<1000 or numero>9999:
    numero = int(input('É entre 1000 e 9999 cara, faz certo: '))
print(f'A unidade é: {str(numero)[3]}')
dezena = str(numero)[2]+'0'
print(f'A dezena é: {dezena}')
centena = str(numero)[1]+'00'
print(f'A centena é: {centena}')
milhar = str(numero)[0]+'000'
print(f'O milhar é: {milhar}')