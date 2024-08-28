class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if(nums.count(nums[i])==1):
                result=result+nums[i]
        return result
  
       