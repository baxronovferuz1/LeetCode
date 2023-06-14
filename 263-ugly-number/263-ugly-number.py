class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        for a in [2,3,5]:
            while n%a==0:
                n=n//a
        return n==1
        


        
        
        
        # if n==2*3 or n==2*5 or n==5*3:
        #     return True
        # return False
        