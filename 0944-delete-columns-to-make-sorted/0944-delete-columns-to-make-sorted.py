class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(1 for i in zip(*strs) if list(i)!=sorted(i))
    
        