class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)

    
        return maxSum / k
        
        
        
        
        
        
        # empty=[]
        # for i in nums:
        #     if i>=k:
        #         resultat=empty.append(i)
        #         added=sum(resultat)
        #         while added<k:
        #             added=resultat/k
        #         return added
                
        