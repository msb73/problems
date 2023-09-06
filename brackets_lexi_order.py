def sol(string):
	if len(string) % 2:
		return False
	stack = []
	dic = {
		'}' : '{',
		')' : '(',
		']' : '['
	}
	for i in string:
		if current :=dic.get(i, False):
			if len(stack):
				if stack[-1] == current:
					stack.pop()
					continue
			else:
				return False
		else:
			stack.append(i)


	if stack:
		return False
	return True

print(sol("}"))


	