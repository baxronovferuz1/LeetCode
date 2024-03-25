class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        xr=0
        for i in range(n):
            nums.append(start+(i*2))
            # nums.append(lists)
        for i in range(len(nums)):
            xr=xr^nums[i]
        return xr
        
        
