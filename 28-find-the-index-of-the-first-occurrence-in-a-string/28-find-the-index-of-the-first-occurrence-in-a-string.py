class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        something=len(needle)
        for i in range(len(haystack)):
            if haystack[i:something+i]==needle:
                return i
        else:
            return -1
        
        
        

