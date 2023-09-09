ls = [10,9,8,7,6,5,4,3,2,1,0]

def quicksrt(ls, start_index, end_index):
	pivot = (end_index + start_index)//2
	p_v= ls[pivot]
	stable_index  = pivot
	# to find the first greater element to swap

	for moving_index in range(start_index, pivot):   
		if ls[moving_index] > p_v:
			stable_index = moving_index
			break

	for moving_index in range(stable_index+1, end_index):
		if ls[moving_index] <= p_v:
			ls[stable_index], ls[moving_index] = ls[moving_index], ls[stable_index]
			stable_index +=1

	if stable_index - start_index > 1:
		quicksrt(ls, start_index, stable_index)
	if end_index - stable_index > 1: 
		quicksrt(ls, stable_index, end_index)

quicksrt(ls, 0, len(ls))
print(ls)
