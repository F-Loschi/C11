nome = input('Qual o seu nome? ')
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' ')-nome.count('\n') - nome.count('\r'))

nome = nome.split()
nome[-1] = 'do Inatel'
nome = " ".join(nome)
print(nome)