class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # mull,subt=1,0
        # while n!=0:
        #     mull*=(n%10)
        #     subt+=(n%10)
        #     n//=10
        # return mull-subt
        
        a=[int(i) for i in str(n)]
        return prod(a)-sum(a)
        