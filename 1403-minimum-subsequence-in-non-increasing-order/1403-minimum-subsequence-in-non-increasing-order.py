class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        answer=[]
        nums.sort()
        while sum(nums)>sum(answer):
            answer.append(nums.pop())
        if sum(nums)==sum(answer):
            answer.append(nums.pop())
        return answer
        