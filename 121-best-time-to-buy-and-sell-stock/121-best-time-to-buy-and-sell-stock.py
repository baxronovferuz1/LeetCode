class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = 10000
        maxDiff = 0
        
        for i in range(len(prices)):
            minVal = min(prices[i], minVal)
            maxDiff = max(prices[i]-minVal, maxDiff)
            
        return maxDiff
        