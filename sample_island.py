row = 6
ls = [[i for i in range(j, j+row)]  for j in range(1,37, 6 )]
for i in ls:
    print(i[0])
