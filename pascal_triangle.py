class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
      ls = [[1]]
      for i in range(1, numRows):
        inner = []
        dup = ls[-1]
        inner.append(1)
        for j in range(i):
          try:
            inner.append(dup[j] + dup[j+1])
          except IndexError:
            inner.append(1)
        ls.append(inner)
      return ls


obj1 = Solution()
print(obj1.generate(10))