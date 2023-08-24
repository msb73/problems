def replace():
	word  = '?s?'
	word = list(word)
	substr = 'a'
	if len(word) < len(substr):
		return '-1'
	count = []
	substr_count = len(substr)-1
	for i in range(len(word)-1,-1,-1):
		if substr_count == -1:
			break
		print('Hello')
		if word[i] == '?' or word[i] == substr[substr_count]:
			
			count.append(i)
			substr_count-=1
			continue
		count = []
		substr_count = len(substr)-1
	if count :
		for i, j  in zip(count[::-1], range(0, len(substr))):
			word[i] = substr[j]
		for i in range(len(word)):
			if word[i] == '?':
				word[i] = 'a'
		return ''.join(word)
	return '-1' 
print(replace())