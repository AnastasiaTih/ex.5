#1
A = [1,2,3,5]
count = 0
for item in A:
    if item >= 4:
        count += 1
print('количество элементов списка, удовлетворяющих данному условию:', count)

#2
N = 5
A = [0] * N
from random import randint
for i in range(N):
    A[i] = randint(0, 50)
print(A)
count = 0
for item in A:
    if item >= 4:
        count += 1
print('количество элементов списка, удовлетворяющих данному условию:', count)