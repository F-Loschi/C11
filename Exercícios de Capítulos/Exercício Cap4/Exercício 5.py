import numpy as np

np.random.seed(10)
arr = np.random.randint(1, 51, 16)
mtz = arr.reshape([4,4])
mediaColunas = mtz.mean(axis = 0)
mediaLinhas = mtz.mean(axis = 1)

for i in range(4):
    print(f"Média da coluna {i} é: {mtz[i].mean()}")
    print(f'Media da coluna {i} é: {mtz[:, i].mean()}')

print(f"A maior média das colunas é: {mediaColunas.max()}")
print(f"A maior média das linhas é: {mediaLinhas.max()}")

unico, i = np.unique(mtz, return_counts=True)

for j in range(len(unico)):
    if unico[j] == 2:
        print(f"{unico[j]} aparece 2 vezes")