n = 4
def fibonacci (n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
s = fibonacci(n)
print(s)