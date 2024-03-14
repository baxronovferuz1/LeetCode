class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_1=[]
        nums_2=[]
        result=[]
        for i in range(n):
            nums_1.append(nums[i])
        
        for i in range(n,2*n):
            nums_2.append(nums[i])
        
        for i in range(n):
            result.append(nums_1[i])
            result.append(nums_2[i])
            
        return result
        
        