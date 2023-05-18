def sort_dic(dic):
	return max(dic, key = lambda x : dic[x][1])

def customer():
	C = [
		[1,2,3],
		[2,3],
		[1,1,4],
		[5]
	]
	dic = {}
	l = 0
	# coding
	C = [[j for j in set(i)] for i in C ]
	for i, ls in enumerate(C):
		for v in ls:
			if v in dic:
				dic[v][0].append(i)   #index of list
				dic[v][1] +=1   # count
			else:
				dic[v] = [[], 1]
				dic[v][0].append(i)
	count = 0
	while len(C):
		# find max
		print(f'\n\n {dic}    {C}')
		maximum = sort_dic(dic)
		# remove count from dic for each dic[0]
		dic0 = dic[maximum][0]
		print(f'\n\n####################{maximum}')
		print(f'dic0 = {dic0}')
		for i in dic0: # i = index of C
			print(f'i = {i}   l = {l}   {len(C)}')
			print(C)
			try:
				for j in C[max(0,i-l)]: # j  = index of C to be decrement from dic 
					dic[j][1] -=1
			except (IndexError, KeyError):
				continue
			print(f' pop  {C.pop(max(0,i-l))}')
			l+=1
		dic.pop(maximum)
		count+=1
	print(count)



customer()
			
		


