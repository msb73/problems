s = 'what are you doing'.split(' ')
t = ('a', 'e', 'i', 'o','u')
s3 = []
for i in range(len(s)):
    s3.append(s[i][0].upper()+ s[i][1:])
print(s3)