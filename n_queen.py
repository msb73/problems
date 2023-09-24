# goes with columns
# n -> input
# i_tups -> all divalidatetion validatons
# validate() -> validateursive func
# validated = {c:r} # as we goes with cols
# 
n = int(input())
# n = 13


counter = 0
dic = {
    1:set(),
    2:set(),
    3:set(),
    4:set()
}
def validate(dic,r, c):   # return T or F for each i_tup for False important, T not
    # print(dic)
    
    global counter
    if c+r in dic[1]:
        return False
    if c-r in dic[2]:
        return False
    if r in dic[3]:
        return False
    if c in dic[4]:
        return False
    return True
# No changes till this


        
# 1 only till this
def dic_add_modification(r,c, dic):
    dic[1].add(c+r)
    dic[2].add(c-r)
    dic[3].add(r)
    dic[4].add(c)

def dic_sub_modification(r,c, dic):
    dic[1].remove(c+r)
    dic[2].remove(c-r)
    dic[3].remove(r)
    dic[4].remove(c)
def nqueen(n:int, marked, rows, dic) -> int:
    if n == 0:
    	return []
    if n == 1:
    	return [["Q"]]
    if n == 2:
    	return [["Q."],[".."]]
    c = 0
    exempted = {}  #2 {}
    while c < n:
        for r in rows:     # data is inputed in marked or not
            if validate(dic, r, c) and not (c,r) in exempted:
                marked[c] = r
                dic_add_modification(r,c, dic)
                rows.remove(r)
                c+=1
                break

        else:
            # print(exempted)
            prev_c = c-1
            # print(marked)
            if not  marked[prev_c]:
                return marked
            prev_r = marked.pop(prev_c)
            dic_sub_modification(prev_r, prev_c, dic)#exempted[(prev_c, prev_r)] = True  exempted.append((prev_r, prev_c))
            exempted[(prev_c, prev_r)] = True
            rows.append(prev_r)
            c-=1
            exempted = {(i):True for i in exempted if i[0] <= c } # 4  exempted = [i for i in exempted if i[1] <= c ]
        # print(exempted)
        # print(marked)
        
        # time.sleep(0.3)

    return marked














rows = list(range(n))
rows[0], rows[1], rows[2] = rows[2] ,rows[0], rows[1]
marked = {}
marked = nqueen(n, marked, rows,dic)
ls = [[ for i in range(n)] for _ in range(n)]

for i , j in marked.items():
    ls[i] [j] = 1

print(counter)