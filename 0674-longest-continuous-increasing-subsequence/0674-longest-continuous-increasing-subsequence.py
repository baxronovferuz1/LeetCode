class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        cur_len = 1         

        max_len = 1  
        
        for i in range(1, len(nums)):
        
            if nums[i] > nums[i-1]:
                cur_len += 1  
                max_len = max(max_len, cur_len)  
            else:
                cur_len = 1  
        
        return max_len
        
        
        
        
        
        
        
        
        