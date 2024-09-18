# Numpy :-

import numpy as np

#create array using numby
arr = np.array([1,2,3,4,5,11,2,5,1,8,44,22,3])
print(arr)
print(type(arr))


print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.sum())
print("before sorting", arr)
arr.sort()
print("after sorting", arr)

def Reverse(arr):
   new_lst = arr[::-1]
   return new_lst


print(Reverse(arr))