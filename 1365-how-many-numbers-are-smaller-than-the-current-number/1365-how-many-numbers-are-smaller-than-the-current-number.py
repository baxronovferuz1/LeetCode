class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index_number=sorted(nums)
        result=[]
        for i in nums:
            result.append(index_number.index(i))
        return result
        