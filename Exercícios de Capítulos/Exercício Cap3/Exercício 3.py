nome = input('Digite o nome do aluno: ')
media = int(input('Digite a média do aluno: '))

aluno = {nome:media}

if aluno[nome] >= 50 :
    print('Aluno aprovado')
    situacao = [media, 'AP']
    aluno = {nome:situacao}
else:
    print('Aluno reprovado')
    situacao = [media, 'RP']
    aluno = {nome: situacao}
print(aluno)