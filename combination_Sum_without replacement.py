ls = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
from functools import lru_cache
ans = 30
main_ls = set()
# @lru_cache
def permut(start, inner_ls, addition):
    for i in range(start, len(ls)):
        if addition + ls[i] > ans :
            break
        temp = inner_ls.copy()
        temp.append(ls[i])
        if addition + ls[i] == ans:
            # print(temp)
            main_ls.add(tuple(temp))
            break
        permut(i+1, temp, addition + ls[i])
permut(0, [], 0)
print(main_ls)
