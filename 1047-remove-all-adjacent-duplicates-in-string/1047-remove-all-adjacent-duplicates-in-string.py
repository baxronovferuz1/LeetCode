class Solution:
    def removeDuplicates(self, s: str) -> str:
        # something=()
        # for i in s:
        #     if i in s:
        #         i.remove(s)
        result=[]
        for i in s:
            if(len(result)>0 and result[-1]==i):
                result.pop()
            else:
                result.append(i)
        return("".join(result))
            
        
        
                
  
        