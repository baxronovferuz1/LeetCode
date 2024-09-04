class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        response= ""
        a=0
        b=0
        while a<len(word1) and b<len(word2):
            response += word1[a]+word2[b]
            a += 1
            b += 1

        response+= word1[a:]+word2[b:]
        return response

