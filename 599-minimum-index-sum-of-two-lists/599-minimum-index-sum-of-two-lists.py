class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lists={}
        for i in list1:
            if i in list2:
                sums=list1.index(i)+list2.index(i)
                lists[i]=sums
        min_value = min(lists.values())
        min_keys = [key for key, value in lists.items() if value == min_value]
        return min_keys
        
        