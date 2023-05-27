class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
                
                
# class Solution(object):
#     def containsDuplicate(self, nums):
#         hset = set()
#         for idx in nums:
#             if idx in hset:
#                 return True
#             else:
#                 hset.add(idx)