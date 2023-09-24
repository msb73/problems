ls = [1,2,3,4,5,6]
ans = 6
main_ls = []
def permut(start, inner_ls, addition):
    for i in range(start, len(ls)):
        if addition + ls[i] > ans :
            break
        temp = inner_ls.copy()
        temp.append(ls[i])
        if addition + ls[i] == ans:
            # print(temp)
            main_ls.append(temp)
            break
        permut(i, temp, addition + ls[i])
permut(0, [], 0)
print(main_ls)