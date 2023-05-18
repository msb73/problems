from inflect import TWO_DIGITS
from more_itertools import one


n = 1000000
def climb(n, memo):
    if n in memo:
        return memo[n]
    if n == 100:
       return 1
    if n > 100:
        return 0
    memo[n] = climb(n+1, memo) + climb(n+2, memo)
    return memo[n]
# print(climb(0,{}))
one = 1
two = 1
for i in range(n-1):
    temp = one
    one = one +two
    two = temp
print(one)