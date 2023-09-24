def find_median(ls, start, end):
	# print(f'{ls[start:end]} start = {start} , end = {end}')
	# print('Hello')
	dic_median = {}
	if end-start > 5:
		for i in range(start+2,end,5):
			# print(f'i = {i}    l = {l}')
			dic_median[ls[i]] = i
		if end-start % 5 !=0:
			dic_median[ls[end-1]] = end-1
		s = sorted(list(dic_median.keys()))
		return dic_median[s[len(s)//2]]
	return (end + start)//2