import time
n = 6
used = True
count = 0
inner_count = 0
ls = [1,3,5,6,7]
ls = [2,3,4,4, 6]
ls.insert(0,ls[0]-1)
print(ls)
main_iter = 0
swap_iter = 0

while swap_iter < n:
	inner_count = 0
	used = True
	while swap_iter< n:
		if ls[swap_iter + 1] - ls[swap_iter] == 1:	
			swap_iter, inner_count  = swap_iter+1, inner_count+1
			# print(f'{ls[swap_iter + 1]} - {ls[swap_iter ]}   {inner_count}')
		elif swap_iter+2 >= n-1:
			# print('false here')
			break 
		elif ls[swap_iter + 2] - ls[swap_iter] == 2 and used:
			inner_count, swap_iter = swap_iter+2, inner_count+2
			used = False

		else:
			print('Treminate HEre')
			break
	
	print(inner_count)
	main_iter = swap_iter+1
	swap_iter = swap_iter+1
	time.sleep(1)

print(count)


