class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_num=sorted(nums)
        return (sorted_num[-1]-1)*(sorted_num[-2]-1)
    
        
        