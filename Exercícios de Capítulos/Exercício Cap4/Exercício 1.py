import numpy as np

arr1 = np.ones(8)
arr2 = np.random.randint(0,9,8)
arr3 = arr1 + arr2
print(arr3.sum())
if arr3.sum() >= 40:
    arr3 = arr3.reshape((4,2))
    print(arr3)
else:
    arr3 = arr3.reshape((2,4))
    print(arr3)