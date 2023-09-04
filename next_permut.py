nums = [6,3,1,2,3,4]
from typing import List

def nextPermutation( nums: List[int]) -> None:
    n = len(nums) 
    for i in range(n-1 , 0, -1):
        if nums[i-1] < nums[i]:
            for k in range(n-1 , i-1, -1):
                if nums[k] > nums[i-1]:
                    nums[k] , nums[i-1] = nums[i-1],  nums[k]
                    break
				
            for j in range(1,((n-i)//2)+1):
                nums[i], nums[n-j] = nums[n-j], nums[i]
                i+=1
            return None
    for i in range((len(nums)//2)):
        nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
        
nextPermutation(nums)

print(nums)