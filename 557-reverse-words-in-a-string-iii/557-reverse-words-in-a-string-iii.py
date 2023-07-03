class Solution:
    def reverseWords(self, s: str) -> str:
        # return  "".join([a[::-1] for a in s.split("")])
        return " ".join([word[::-1] for word in s.split(" ")])
        