class Solution:
    def maxDepth(self, s: str) -> int:
        nesting_depth=[]
        max_l=0
        
        for i in s:
            if i=="(":
                nesting_depth.append(i)
                if len(nesting_depth)>max_l:
                    max_l=len(nesting_depth)
                
            elif i==")":
                nesting_depth.pop(-1)
        return max_l