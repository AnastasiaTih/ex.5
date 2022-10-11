A = [1,2,3,5]
count = 0
min_min = 10
delta = 4
for item in range(len(A)):
    if A[item] < min_min:
        min_min = A[item]
for item in range(len(A)):
    if min_min + delta == A[item]:
        count += 1
print('количество элементов списка, удовлетворяющих данному условию:', count)
