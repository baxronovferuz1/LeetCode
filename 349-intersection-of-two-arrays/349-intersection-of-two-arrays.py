class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #return set(nums2) & set(nums1)
        return set(nums2).intersection(nums1)
        