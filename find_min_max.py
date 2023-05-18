# Find Min and Max in 2(N-2) TIme complexity
ls = [63,34,12,34,23,5,346,31,2,32,5,1,10000]
def find(l, g, i, c):
    try:
        c+=1
        if ls[l] < ls[i]:

            print(f'{ls[l]}    {ls[i]}')
            c+=1
            if ls[g] < ls[i] :
                g = i
        else:
            l = i
        i+=1
    except IndexError:
        return (ls[l], ls[g], c)
    return find(l,g,i, c)
print(find(0,0,0,0))



 