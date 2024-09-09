class Solution:
    def reverseWords(self, s: str) -> str:
        reverse=s.split()
        result=reverse[::-1]
        return " ".join(result)
      