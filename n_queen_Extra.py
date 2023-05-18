# goes with columns
# n -> input
# i_tups -> all divalidatetion validatons
# validate() -> validateursive func
# validated = {c:r} # as we goes with cols
# 
n = 15
import time
i_tups = (
    (-1,-1),
    (-1,0),
    (-1,1),
    (1,-1),
    (0,-1),
    (0,1),
    (1,1),
    (1,0)
    
)
counter = 0
def validate(i_tup, r, c, marked):   # return T or F for each i_tup for False important, T not
    if marked.get(c) == r:
        return (False, r, c)
    if r > n-1 or c > n-1 or r < 0 or c < 0:
        return (True, r, c)
    global counter
    counter +=1
    return validate(i_tup, i_tup[0] + r, i_tup[1]+ c, marked)
# No changes till this

def iter_through_tuple(r,c, exempted, marked):   # return the whole T or F for whole r
    for i_tup in i_tups:
        validate_return = validate(i_tup, r, c, marked)
        # print(validate_return)
        if not validate_return[0]:
            return False
    else:
        if exempted.get((c,r)):  #1  exempted[c] == r  (r,c) in exempted
            return False
        marked[c] = r
        return True
        
# 1 only till this
        
def nqueen(n:int, marked, rows) -> int:
    c = 0
    exempted = {}  #2 {}
    while c < n:
        for r in rows:     # data is inputed in marked or not
            cond = iter_through_tuple(r,c, exempted, marked)
            if cond:
                rows.remove(r)
                c+=1
                break

        else:
            # print(exempted)
            prev_c = c-1
            prev_r = marked.pop(prev_c)
            exempted[(prev_c, prev_r)] = True   #3 exempted[prev_c] = prev_r   exempted.append((prev_r, prev_c))
            rows.append(prev_r)
            c-=1
            exempted = {(i):True for i in exempted if i[0] <= c } # 4  exempted = [i for i in exempted if i[1] <= c ]
            # print(exempted)
        # print(marked)
        
        # time.sleep(0.3)

    return marked














rows = list(range(n))
rows[0], rows[1] = rows[1], rows[0]
marked = {}
marked = nqueen(n, marked, rows)
print(f'{len(marked)} = *{marked}')

print(counter)