#Definições
i=0 #Contador
nome = "" #Variável pro nome
peso = 0  #Variável pro peso
pesomax = -1
pesomin = 1000
pessoas = {}  #Dicionário
#Inserindo e definindo
for i in range(3):
    nome = input("Informe o seu nome: ")
    peso = int(input("Informe o seu peso: "))
    if peso<pesomin:
        pesomin = peso
    if peso>pesomax:
        pesomax = peso
    pessoas[peso] = nome
#Mostrando
print(f"Pessoa mais pesada: {pessoas[pesomax]}")
print(f"Pessoa mais leve: {pessoas[pesomin]}")