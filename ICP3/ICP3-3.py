import numpy as np
#arr= np.random.randint(low=1, high=20, size=15, r)
arr = np.random.choice(range(1,21), 15, replace=False)
print(arr)
max= np.amax(arr)
arr2 = np.where(arr==max, 0, arr)
print(arr2)
