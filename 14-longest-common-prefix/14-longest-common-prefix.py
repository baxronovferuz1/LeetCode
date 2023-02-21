class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        assert len(strs) > 0
        prefix = min(strs,key=len)
        while not all(s.startswith(prefix) for s in strs):
            prefix = prefix[:-1]
        return prefix
        