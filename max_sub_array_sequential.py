#O(1)

def maxSubArray(nums: list[int]) -> int:
    sum = nums[0]
    counter = nums[0]
    for i in range(1, len(nums)):
        counter+=nums[i]
        if counter  < nums[i]:
            counter =  nums[i]
        if counter > sum :
            sum = counter
    return sum

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
