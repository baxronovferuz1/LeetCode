class Solution:
  def compress(self, chars: List[str]) -> int:
    empty = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[empty] = letter
      empty += 1
      if count > 1:
        for c in str(count):
          chars[empty] = c
          empty += 1

    return empty

        
        