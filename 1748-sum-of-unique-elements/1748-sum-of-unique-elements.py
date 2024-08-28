class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            if(nums.count(nums[i])==1):
                sum=sum+nums[i]
        return sum
  
        # sum = 0
        # for i in range(len(nums)):
        #         if(nums.count(nums[i]) == 1):
        #                 sum = sum + nums[i]
        # return sum