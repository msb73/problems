ls = [1, 2, 3, 5]
ans = 10
count = 0
def func1(arr, subls, index, adder):
	for i in range(index, len(ls)):
		if adder + ls[i] == ans:
			arr.append(subls + [ls[i]])
			# return subls + [ls[i]]
			return None
		if adder + ls[i] > ans:
			return None
		func1(arr, subls + [ls[i]], i, adder + ls[i] )
	return arr

print(func1([], [], 0, 0))



# break sattement -> if sum(arr) == ans or sum(arr)  > ans: break

# for i in ls:
#     def rec(subls , index, sum):
# 		subls.append(ls[index])
# 		if break condition
#             break
		
# 		rec(subls, index+1)

# for i in ls:
# 	subls = [1]
# 	subls = [2]
# 	subls = [3]
	
# 	rec(subls, index, sum)

