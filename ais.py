
# def solve(n,s):
#     for i in s:
#         if i == '1':
#             return 'YES'
#     return 'NO'
N = 4
l = [
    [1,2],
    [2,3],
    [4.3]
]
# from 1 -> 3
for i in l:
    pass
ls = [[1,2,4], [2,3,4], [4,3,2]]
dict = {i: 0 for i in range(1,N+1) }
print(dict)
for i in ls:
    dict[i[0]] += i[2]
    dict[i[1]] -= i[2]
print(dict)