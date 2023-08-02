class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lists=[]
        for i in operations:
            if i=="D":
                lists.append(2*lists[-1])
            elif i=="C":
                lists.pop()
            elif i=="+":
                lists.append(lists[-1]+lists[-2])
            else:
                lists.append(int(i))
        return sum(lists)
            
        
        
        
        
        
        
    
      