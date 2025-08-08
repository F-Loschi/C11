print('Seja bem vindo a sua calculadora de gasto de gasolina!')
print('Para viagens até 200km, será cobrado R$0,50. Para viagens mais longas, R$0,45.')
kilometragem = int(input('Quantos kilometros deseja calcular? '))
if kilometragem <= 200:
    print(f'Você pagará {kilometragem*0.5} em gasolina')
else:
    print(f'Você pagará {kilometragem*0.45} em gasolina')