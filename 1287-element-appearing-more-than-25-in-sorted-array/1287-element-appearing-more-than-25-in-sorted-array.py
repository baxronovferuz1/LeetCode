class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        something=(len(arr)*25)/100
        for i in arr:
            result=arr.count(i)
            if result>something:
                return i
        