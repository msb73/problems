from functools import lru_cache
ls = [41,6,16,24,31,40,44,22,15,9,29,3,31,10,50,44,39,47,45,47]
target = 39
counter = 0
dic = {}
def permut(i, amount):
    if (i, amount) in dic:
        # 
        return dic.pop((i, amount))
    global counter
    counter+=1
    if i == len(ls):
        return 1 if amount == target else 0
    result =  permut(i+1, amount + ls[i]) + permut(i+1, amount - ls[i])
    dic[(i, amount)] = result
    return result
print(permut(0, 0))
print(counter)



