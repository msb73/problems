# ls = [
#     (2,1,72),
#     (2,5,50),
#     (2,3,21),
#     (1,2,22),
#     (2,5,16),
#     (1,5,17),
#     (1,4,79)
    
# ]

ls = [
    (2,2,91),
	(2,5,89),
    (2,5,63),
    (1,4,34),
    (1,1,4)
]
n = 5

# 1 = row
# 2 = col
sum = 0
lrow = []
lcol = []
for i in ls[::-1]:
    if i[0] == 1:
        if i[1] in lrow:
            continue
        else:
            sum+= i[2]* (n-len(lcol))
        lrow.append(i[1])
    else:
        if i[1] in lcol:
            continue
        else:
            sum+= i[2]* (n-len(lrow))
        lcol.append(i[1])
print(sum)
