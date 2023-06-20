class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # return range(sorted(nums+1)))-int(range(sorted(nums)))
        
        return set(range(1,len(nums)+1))-set(nums)
        
        