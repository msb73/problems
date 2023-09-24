# ls = list(range(1000, 0, -1))
# ls = [324,23,4,214,2,4,324,235,34,64,56,5,32,4,23,41,23,4235,34,4,56,57,65,74,2,3,23,42,314,4,34,23,43,5,345,34]
ls = [1,2,3,4,5,6,7,8,9,0]
# from linear_median import find_median


c = 0
def quicksrt(ls, start_index, end_index):
	global c
	print(ls)
	pivot = (end_index + start_index)//2
	# pivot = find_median(ls, start_index, end_index)
	p_v= ls[pivot]
	# print(f' pivot = {pivot}')
	stable_index  = pivot
	# to find the first greater element to swap

	for moving_index in range(start_index, pivot):   
		c+=1
		if ls[moving_index] > p_v:
			stable_index = moving_index
			break

	for moving_index in range(stable_index+1, end_index):
		c+=1
		if ls[moving_index] <= p_v:
			ls[stable_index], ls[moving_index] = ls[moving_index], ls[stable_index]
			stable_index +=1
	# print(f'start = {start_index}   stable = {stable_index}   end = {end_index}   p_v == {p_v} ')
	if stable_index - start_index > 1:
		# print('H')
		quicksrt(ls, start_index, stable_index)
	if end_index - stable_index > 1: 
		
		quicksrt(ls, stable_index, end_index)

quicksrt(ls, 0, len(ls))
# print(131952)
print(c)

# print(ls)
