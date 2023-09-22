class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x=iter(t)
        return all(ch in x for ch in s)
    
        # tt=iter(t)
        # for i in s:
        #     if i in tt:
        # return all(i)
        