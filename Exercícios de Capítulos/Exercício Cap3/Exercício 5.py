pessoas = {}
nome = ""
idade = 0
sexo = ""
somaIdade = 0
i = 0
iMulheres = 0
n = int(input("Diga quantas pessoas você deseja entrar: "))

for i in range(n):
    nome = input(f"Digite o nome da {i+1}° pessoa: ")
    idade = int(input(f"Digite a idade dessa pessoa: "))
    somaIdade += idade
    sexo = input(f"Digite o sexo dessa pessoa(M/F): ")
    if sexo == "F" and idade < 20:
        iMulheres += 1
    pessoas[nome] = [idade, sexo]

print(f"A média de idade das pessoas do grupo é: {somaIdade/n}")
print(f"Há {iMulheres} mulheres com menos de 20 anos")