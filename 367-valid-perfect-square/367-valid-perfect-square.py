class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num)==floor(sqrt(num))
        
        
        # for i in range(100000000):   :)
        #     if i*i==num:
        #         return True
        # else:
        #     return False