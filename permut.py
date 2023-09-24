
ls = [1,2,3, 4, 5, 6, 7]
len_ls = len(ls)
r = 4

def permutation(ls, r):
	perm_cons = list(range(r))
	result = []

	while True:
		temp_ls = [ls[i] for i in perm_cons]
		
		for i in range(perm_cons[-1], len_ls):
			temp_ls[-1] = ls[i]
			result.append(temp_ls.copy())

		if result[-1][0] == ls[-r]:
			return result

		for b, f in zip(range(r - 2, -1, -1), range(len_ls-2,0,-1)):
			if perm_cons[b] < f:
				last_value = 	perm_cons[b] 
				for i in range(b, r):
					perm_cons[i] = last_value +1
					last_value+=1
				break
print(permutation(ls, r))
