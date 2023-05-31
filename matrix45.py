matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
ls = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
        	ls.append((i,j))
print(ls)
for i, j in ls:
    for k in range(len(matrix[0])):
        matrix[i][k] = -1
    for l in range(len(matrix)):
        matrix[l][j] = -1
        
# m[0][5] = 0
print(matrix)