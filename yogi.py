n = 4
q = 3
a = [1,2,1,1]

sum = 0
queries = [[1,2],[1,2], [2,3], [3,4]]
dic = {}

def add_dic(index, dic):
	for i in index:
		try:
			dic[i] += 1
		except KeyError:
			dic[i] = 1

for query in queries:
	inner_dict = {}
	a_query = a[query[0]-1: query[1]]
	inner_dict = {i:[] for i in a_query}
	for index, val in  enumerate(a_query):
		inner_dict[val].append(index+query[0])
	sum += len(inner_dict)
	for v in inner_dict.values():
		if len(v) > 1:
			add_dic(v, dic)

sum +=max(dic.values())