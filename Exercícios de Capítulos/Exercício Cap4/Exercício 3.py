import numpy as np

def jogada(campo:np.array([2,2])) -> None:
    print("Bem vindo ao campo minado!")
    i = int(input(("Para jogar, digite qual linha você deseja: ")))
    j = int(input(("Beleza, agora a coluna: ")))
    tentativas = 0
    acabou = False
    print(f"Você jogou nas posições ({i}, {j})")
    while acabou == False:
        if (campo[i][j] == 1):
            print("Bum, explodiu! Ela trocou, me pediu!")
            print("Game Over! :( Try Again!")
            acabou = True
        else:
            print("Ow yeah baby, aqui não tem bomba, tenta de novo")
            tentativas += 1
            if tentativas == 3:
                acabou = True
                break
            i = int(input(("Qual linha tu vai agora?: ")))
            j = int(input(("Beleza, e a coluna: ")))
    if tentativas == 3:
        print("Congratulations! You beat the game! :)")




campo = np.zeros([2,2])
i = np.random.randint(0,2)
j = np.random.randint(0,2)
campo[i][j] = 1
jogada(campo)

