n = 2
def func(n):
    b = bin(n)
    for i in range(len(b)):
        try:
            s = b[i] + b[i+1]
            if s == '10' or s == '01':
                return 'Yes'
        except IndexError:
            return 'No'
print(func(n))