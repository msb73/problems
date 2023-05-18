# n = 2
# dir = {
#     'abcd': 'ac',
#     'pppp': 'p'
# }
# file = open('test_set_1/ts1_input.txt', 'r')
# file1 = open('test_set_1/ts1_output.txt', 'r')
# ls1 = file.readlines()[1:]
# ls2 = file1.readlines()
# counter = 0
# ans = []
# for i in range(100):

#     su = 0
#     string = [ord(j) for j in ls1[counter]]
#     counter+=1
#     x = [ord(j) for j in ls1[counter]]
#     counter+=1
#     for j in string:
#         su += min([abs(j-k) for k in x])      
#     if f'Case #{i}: {su}' != ls2[i]:
#         print(f'{su}        {ls2[i]}')
    # x = (lambda x : min(  abs(ord(i)*len(x[0]) - sum([ord(j) for j in x[0]])) for i in x[1]     )    )((input(), input()))
    # print(x) 
# print(sum([ord(i) for i in 'pqrst']))

for i in range(int(input())):
    su = 0
    string = [ord(j) for j in input()]
    x = [ord(j) for j in input()]
    for j in string:
        ls = []
        for k in x:
            if abs(j - k) == 25:
                ls.append(1)
            else:
                ls.append(abs(j-k))
        su += min(ls)
        # su += min([abs(j-k) for k in x])      
    print(f'Case #{i+1}: {su}')
  
