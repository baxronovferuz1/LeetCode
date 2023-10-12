class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        for char in words[0]:
            for i in range(1, len(words)):
                if char in words[i]:
                    words[i] = words[i].replace(char, '', 1)
                else:
                    break
            else:
                result.append(char)

        return result
        