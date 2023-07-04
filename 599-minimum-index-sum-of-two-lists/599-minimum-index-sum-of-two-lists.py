class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l={}
        for i in list1:
            if i in list2:
                sums=list1.index(i)+list2.index(i)
                l[i]=sums
        min_value = min(l.values())
        min_keys = [key for key, value in l.items() if value == min_value]
        return min_keys
        
        