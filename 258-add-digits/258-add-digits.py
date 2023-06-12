class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            num = sum(int(i) for i in str(num))
        return num
    
    
    
#         list_1=[]
#         while num<0:
#             for i in num:
#                 list_1=append(i)
#             return list_1
        