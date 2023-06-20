class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))<3:
            return max(nums)
        return sorted((set(nums)),reverse=True)[2]
        
        
        # if len(nums)>=3:
        #     nums=sorted(set(nums),reverse=True)
        #     # num=nums[2]
        #     return nums[2]
        # else:
        #     return max(nums)
        
        
        
        
        
        # if nums[2] not in nums:
        #     return nums[-1]
        # else:
        #     return nums[2]