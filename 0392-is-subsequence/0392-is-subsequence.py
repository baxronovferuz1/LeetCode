class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # x=iter(t)
        # return all(ch in x for ch in s)
    
     

        i=0
        j=0

        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1

        if i==len(s):
            return True
        else:
            return False
        