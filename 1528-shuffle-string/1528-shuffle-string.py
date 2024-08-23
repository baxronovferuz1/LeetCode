class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x=""
        for i in range(len(s)):
            x=x+s[indices.index(i)]
        return x