t = ((-1, 0),(0, +1),(+1, 0),(0, -1))

	# main_c = []
	# def permut(i, count):
	#     if i[0] == len(ls)  or i[1] == len(ls[0]) or i[0] < 0 or i[1] < 0:
	#         print(i > (0,-1))
	#         return count
	#     if ls[i[0]][i[1]] in (0,2):
	#         return count
	#     count +=1
	#     ls[i[0]] [i[1]] = 2
	#     inner_count = 0
	#     for index in t:
	#         curr_count = permut((i[0] + index[0], i[1] + index[1]), count)
	#         if inner_count < curr_count:
	#             # print(f'{inner_count = }')
	#             inner_count = curr_count
	#     return inner_count


	# def find_i(ls, find):
	# 	for i in range(len(ls)):
	# 		for j in range(len(ls[0])):
	# 			if ls[i][j] == find:
	# 				return (i,j)
	# 	return 0

	# ls = [[0,2]]
	# i = find_i(ls, 2)

	# ls[i[0]][i[1]] = 1

	# ans = permut(i, 0)
	# print(ans)
	# print(ls)
	# if find_i(ls, 1):
	#     print(-1)
	# else:
	#     print(ans-1)
ls = [[2,1,1],[1,1,0],[0,1,1]]
ls = [[2],[1]]
# ls = [[2,1,1],[1,1,1],[0,1,2]]
# ls = [[0]]
# ls = [[1]]
def permut():
    
    ROWS, COLS = len(ls), len(ls[0])
    s = {ROWS, COLS, -1, COLS +1}
    fresh = 0
    maximum = 0
    q = []
    for i in range(ROWS):
    	for j in range(COLS):
    		if ls[i][j] == 1:
    			fresh+=1
    		elif ls[i][j] == 2:
    			q.append((i,j))
    if fresh == 0:
        return 0
    while q :
        r, c = q.pop(0)
        for t_r, t_c in t:
            inner_counter = 0
            n_r, n_c = r + t_r, c + t_c
            # if n_r in s or n_c in s:
            if n_r == ROWS or n_c == COLS or n_r < 0 or n_c < 0:
                print(n_r, n_c)
                continue
            if ls[n_r] [n_c] == 1:
                fresh -=1
                ls[n_r] [n_c] = ls[r] [c]+1 
                maximum = ls[n_r] [n_c]
                q.append((n_r, n_c))   
    if fresh != 0 :
        return -1
    return maximum - 2

ans = permut()
print(ans)