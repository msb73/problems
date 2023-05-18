n = 8
ls = []
for i in range(n):
    ls.append([(i-j) for j in range(n)])
for i in ls:
    print(i)
        
    
# \ i-j
# / i+j
# -- r
# |  c