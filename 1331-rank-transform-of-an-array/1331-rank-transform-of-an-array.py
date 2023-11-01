class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        something = {}
        sort_arr = sorted(set(arr))

        for i in range(len(sort_arr)):
            something[sort_arr[i]] = i+1

        
        for i in range(len(arr)):
            arr[i] = something[arr[i]]
        
        return arr
        