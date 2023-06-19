class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # for i in s:
        #     if t.count(i)==s.count(i):
        #         return True
        
        i=0
        for let in t:
            if i==len(s):
                return True
            if s[i]==let:
                i+=1
        return i==len(s)
        