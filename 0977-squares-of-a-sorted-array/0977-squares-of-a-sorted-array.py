class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return list(sorted(nums)**2) 
        abc=[]
        for i in nums:
            abc.append(i**2)
        return sorted(abc)
    
        # for i in range(len(nums)):
        #     nums[i]=nums[i]*nums[i]
        # nums.sort()
        # return nums