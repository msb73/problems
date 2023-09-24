# ls = [32423,41,5,124,53,64,57,74,6,236,45,756,8,6,45,634,5324,5,1]
ls = list(range(-23,0))
l = len(ls)
def l_sort(temp1, temp2):
	print(f'{temp1=}  {temp2=}')
	temp = []
	t1 = 0
	t2 = 0
	# print(f'{t1= }   {t2=}')
	try:
		while True:
			if temp1[t1] < temp2[t2]:
				temp.append(temp1[t1])
				t1 += 1
			else: 
				temp.append(temp2[t2])
				t2 += 1
	except IndexError:
		if t1 == len(temp1):
			temp.extend(temp2[t2:])
		else: 
			temp.extend(temp1[t1:])
	return temp
    
def merge(ls):
    step = 2
    while True:
    	for i in range(0, len(ls), step):
        	ls[i: i+step] = l_sort(ls[i: i+(step//2)], ls[i+step//2: i + step])
    	if step > len(ls):
    	    break
    	step *= 2
merge(ls)
print(ls)