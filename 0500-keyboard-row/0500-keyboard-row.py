class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line_1="qwertyuiop"
        line_2="asdfghjkl"
        line_3="zxcvbnm"
        result=[]
        for i in words:
            word=i.lower()
            if len(set(line_1+word))==len(line_1) or len(set(line_2+word))==len(line_2) or len(set(line_3+word))==len(line_3):
                result.append(i)
        return result
        
        
       
        
        
        
        
        
        
        
        