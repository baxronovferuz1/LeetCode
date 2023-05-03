class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        obj1,obj2=set(nums1),set(nums2)
        return obj1-obj2,obj2-obj1
        
