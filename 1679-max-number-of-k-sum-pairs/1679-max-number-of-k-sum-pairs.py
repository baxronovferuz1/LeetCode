from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result=0
        count=Counter()
        
        for num in nums:
            compliment=k-num
            if count[compliment]>0:
                result+=1
                count[compliment]-=1
            else:
                count[num]+=1
        return result       