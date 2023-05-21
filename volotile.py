T = 2
def solve(N, Q, pairs, A):
    dic = {}
    indexdic = {}
    t_count = 0
    same_keys = 0
    for i in range(len(A)):
        if indexdic.get(A[i]):
            indexdic[A[i]].append(i)
        else:
            indexdic[A[i]] = [i]
    print(indexdic)
    for pair in pairs:
        dic[pair] = []
        i = 0
        j = 0
        while True:
            if indexdic[pair[0]][i] < indexdic[pair[1]][j]:
                dic[pair].append(pair[0])
                i +=1
            else:
                dic[pair].append(pair[1])
                j+=1
                
        # pdic[pair] = []
        # p1len = len(dic[pair[0]])
        # p2len = len(dic[pair[1]])
        # for i, j in zip(dic[pair[0]]):
        for i in A:
            if i in pair:
                dic[pair].append(i)
    for key, values in dic.items():
        count1 = values.count(key[0])
        count2 = values.count(key[1])
        if key[0] == key[1]:
            same_keys += (count2 * (count2+1))//2
        for i in values:
            if i == key[0]:
                print(f'{i} -> {count2}') 
                t_count +=count2
            else:
                count2 -=1
            if not count2 :
                break     
    # print(t_count)
    return t_count - same_keys
print(solve(1, 2, [(9,5), (1, 1), (10, 10)], [9, 5, 10, 9, 1, 9, 5, 1, 10, 5]))