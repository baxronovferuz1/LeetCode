class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans=-1
        for x,y in enumerate(s):
            for a,b in enumerate(s):
                if y==b and x!=a:
                    ans=max(ans,abs(x-a)-1)
        return ans 
        
        