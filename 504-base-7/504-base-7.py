class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0: 
            return "0"
        a=''
        if num<0:
            num=-num
            a = '-'
        num7 = ''
        while num>0:
            num7+=str(num%7)
            num = num//7
        return a+num7[::-1]
        