import numpy as np

arr = np.random.randint(0, 10, (3, 3))
print(arr)

i, j = arr.shape

if i * j % 2 == 0:
    print("Essa matriz poderia ser um vetor unidimensional com um número par de elementos")
else:
    print("Essa matriz poderia ser um vetor unidimensional com um número ímpar de elementos")