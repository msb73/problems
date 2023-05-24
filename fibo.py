# n = 4
# def fibonacci (n):
#     if n == 1 or n == 2:
#         print(n)
#         return 1
    
#     s = (fibonacci(n-1) + fibonacci(n-2))
#     print(s)
#     return s
# s = fibonacci(n)
# print(s)

def fibo(n):
    print(f'Before  -->  {n}')
    if n == 1:
        return 1
    
    s = fibo(n-1)
s = fibo(5)
print(s)
    