n = 100000000
n = list(str(n))
for i in range(len(n)%3,len(n),4):
    n.insert(i,',')
if n[0] == ',':
    print(''.join(n[1:]))
print(''.join(n))