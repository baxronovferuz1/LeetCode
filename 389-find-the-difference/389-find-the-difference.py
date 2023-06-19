class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i)!=t.count(i):
                return i
    
        
        
    	# s, t = sorted(s), sorted(t)
    	# for i in range(len(t)):
    	# if t[i] not in s[i]:
    	# return t[i]