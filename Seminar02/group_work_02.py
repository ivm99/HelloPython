# N = int(input("Введите число: "))
# print(f"Для N={N} -> ", end= "")
# for i in range(0,N-1):
#     print((-3)**i, end= ", ")
# else:
#     print((-3)**(N-1))

######################################################################

# A = [1, 2, 3, 8, 9, 10]
# sum = 0
# poz_min = 0
# poz_max = 0
# i = 1
# size = len(A)
# while i < size:
#     if A[i] > A[poz_max]:
#         poz_max = i
#     elif A[i] < A[poz_min]:
#         poz_min = i   
#     i += 1
# print(poz_min, poz_max)
# if poz_max > poz_min:
#     for i in range(poz_min, poz_max+1):
#         sum = sum + A[i]
# elif poz_max < poz_min:
#     for i in range(poz_max, poz_min+1):
#         sum = sum + A[i]   
# else:
#     sum = A[poz_max]
# print(A, sum)

####################################################################

A = [2, 3, 6, 98, 56, 45, 78, 100, 49]
max = A[0]
for i in A[1:]:
    if i > max:
        max = i
count = 0
for i in A:
    if  max*0.9 < i and i !=max:
        count += 1 
print(count)
