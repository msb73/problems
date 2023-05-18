# ls = [
#     [39, 1],
#     [20, 0],
#     [21, 0],
#     [12, 0]
# ]


# ls = [
#     [8737,0],
#     [5968,1],
#     [7116,1],
#     [1224,0],
#     [3954,1],
#     [3418,0],
#     [204,0],
#     [2565,0],
#     [8283,1]
# ]

ls = [
    [12,1],
    [2000,1],
    [1000,1],
    [3000,0],
    [100000,0]
]
# 1 mine right
# 0 mine left

n = 9

def check_collision(val1, val2, index1, index2):
    if val1[1] - val2[1]:         # to be collide
        if val1[0] - val2[0] == 0:
            return (index1, index2-1)   # index2-1 because index changes after pop element in ls
        elif val1[0] - val2[0] > 0:
            val1[0] = val1[0] - val2[0]
            return (index2,)
        else:
            val2[0] = val2[0] - val1[0]
            return (index1,)


def delete_index(ls, indexes):
    for index in indexes:
        print(f'tobepop		{ls[index]}')
        ls.pop(index)


i = 0
while i < n-1:
    try:
        if ls[i][1] - ls[i+1][1] >0:
            print(ls[i], ls[i+1])
            indexes = check_collision(ls[i], ls[i+1], i, i+1)
            delete_index(ls, indexes)
            if i:
                i -= 1
        else:
            i += 1
    except IndexError:
        print(ls)
        break
