class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # if heights != sorted(heigh):
        #     return 0
        # else:
        expected=sorted(heights)
        count=0
        for i in range(len(heights)):
            if expected[i]!=heights[i]:
                count+=1
        return count
        
        
        
        
      