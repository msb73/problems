ls = [2,3,5]
answer = 8
arr = []
mainarr = []
for i in range(3):
    arr.extend([ls[i]]*(answer // ls[i]))
print(arr)



from itertools import combinations_with_replacement
print(list(combinations_with_replacement([1,2,3,4,5],3)))

