class Solution:
	def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
		candidates.sort()
		arr = []
		def func1( sub, index, adder):
			for i in range(index, len(candidates)):
				# print(f'{adder + candidates[i]}		{sub + [candidates[i]]}')
				if adder + candidates[i] == target:
					arr.append(sub + [candidates[i]])
					return arr
				if adder + candidates[i] > target:
					del sub
					break
				func1( sub + [candidates[i]], i, adder + candidates[i] )
			# print(arr)
			return arr
		return func1( [], 0, 0)



# break sattement -> if sum(arr) == ans or sum(arr)  > ans: break

# for i in ls:
#     def rec(subls , index, sum):
# 		subls.append(ls[index])
# 		if break condition
#             break
		
# 		rec(subls, index+1)

# for i in ls:
# 	subls = [1]
# 	subls = [2]
# 	subls = [3]
	
# 	rec(subls, index, sum)

# class Solution:
#     def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
#         # target = 9
# 		#candidates = [2, 3, 5]
#         cache = [[] for _ in range(target + 1)]  # empty list of target length -> [[], [], [], [], [], [], [], [], [], []]

#         cache[0] = [[]]    
#         for c in candidates:
#             for i in range(target + 1):
#                 if i >= c: # becaue you can only add combinations if target (i) is greater
#                     for temp_ans in cache[i - c]:   # or i = 2  -> 0 
#                         print(f'{i} -  {c}     {temp_ans}')
#                         cache[i].append(temp_ans + [c])
#                         print(cache)
#         return cache[-1]
# obj1 = Solution()
# obj1.combinationSum([2, 3, 5], 9)