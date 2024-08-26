class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_num=[]
        count_num=Counter(arr)
        for i in count_num:
            if count_num[i]==i:
                lucky_num.append(i)
        if len(lucky_num)==0:
            return -1
        else:
            return max(lucky_num)
        
        
        
        
        
        
        
        
        
      
        