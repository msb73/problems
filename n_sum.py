import time
ls = [1,2,3,4,6]
value =500
ans = []
ls1 = [[[i], v] for i,v in enumerate(ls) ]
for i in range(len(ls1)): # main iterate through ls
    if ls1[i][1] > value-1: # if sum > value (v-1 to check ==) drop before next for loop and continue
        if	ls1[i][1] == value:
            ans.append(ls1[i][0])
        ls1.pop(i)
print(ls1)
while len(ls1):
    for last_index in range(ls1[0][0][-1]	, len(ls)):
        templs = ls1[0][0]
        tempval = ls1[0][1]
        if tempval+ ls[last_index] < value:
            temp2 = [templs[:], tempval]
            temp2[0].append(last_index)
            temp2[1] += ls[last_index]
            ls1.append(temp2)
            continue
        elif tempval + ls[last_index] == value:
            templs.append(last_index)
            ans.append(templs)
        ls1.pop(0)
        break
        
                
        
        
# for i in ls1:
	# for j in ls[ls1[0][-1]]:
#		if ls[]#
# termiantion statements
	#if ls1[i][0][-1] == 4:
	#if ls[i][1] >= 6:
	#  