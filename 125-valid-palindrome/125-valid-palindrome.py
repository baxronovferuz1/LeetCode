class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = ''.join(i for i in s if i.isalnum()).lower()
        return valid[::-1] == valid
    