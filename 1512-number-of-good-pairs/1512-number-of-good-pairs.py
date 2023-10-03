class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
                return sum([((nums.count(i)-1)*(nums.count(i))//2) for i in set(nums) if nums.count(i)>1])
        