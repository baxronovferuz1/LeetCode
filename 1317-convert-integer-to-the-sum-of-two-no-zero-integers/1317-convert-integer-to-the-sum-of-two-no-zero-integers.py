class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]: 
        def check_number(cl):
            while cl>0:
                if cl%10==0:
                    return False
                cl//=10
            return True
        for a in range(1, n):
            b=n-a
            if check_number(a) and check_number(b):
                return [a,b]