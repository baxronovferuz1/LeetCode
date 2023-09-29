class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        right = True
        reverse = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                reverse = False
            elif nums[i] < nums[i - 1]:
                right = False

        return right or reverse
        