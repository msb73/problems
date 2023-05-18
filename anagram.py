def is_anagram(str1, str2):
    dic = {}
    if len(str1) != len(str2):
        return False
    for i,j in zip(str1,str2):
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
        if j in dic:
            dic[j] -=1
        else:
            dic[j] = -1
    if max(dic.values()) or min(dic.values()):
        return False
    return True