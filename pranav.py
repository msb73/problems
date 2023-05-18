# string = input()
# ls = string.split(' ')
# ls = sorted(ls, key= lambda x : len(x), reverse=True)

# def func():
#     length = 0     #this one
#     for i in range(0,len(ls)+1):
#         for j in range(i+1,len(ls)):
#             if len(set(list(ls[i])).intersection(set(list(ls[j])))) == 0:
#                 if len(ls[i]) * len(ls[j]) > length:   # this one
#                     length = len(ls[i]) * len(ls[j])   
#     return length      

# print(func())
# N, X = input().split(' ')
# ls = [int(i) for i in input().split(' ')]
# ls = [1,2,3,4,5]
# from itertools import combinations

# for i in (combinations(ls,4)):
    # print(i)
#     if sum(i) == int(X):
#         print(1)
#         break
# else:
#     print(0)
N = int(input(),2)
print(N)
counter = 0
while True:
    if N == 0:

        print(counter)
        break
    counter +=1
    if N % 2 == 0:
        N = int(N/2)
    else:
        N = N-1
    