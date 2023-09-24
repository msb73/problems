
arr = [1,2,3,4,5,6,7,8,9,10,20,21,34,4523,523,6,2456,234,5,5,235]
def gcd(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+i):
            try:
                if arr[j] % arr[i] == 0:
                    break
            except IndexError:
                return arr[i]
    return -1                
print(gcd(sorted(set(arr))))
