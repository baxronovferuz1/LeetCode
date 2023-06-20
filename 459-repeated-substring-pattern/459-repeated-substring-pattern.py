class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # return s in s[1:] + s[:-1] 
        
        if re.search(r'^(.+)\1+$', s) :
            return True
        else:
            False
        