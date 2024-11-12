class Solution:
    def maximum69Number (self, num: int) -> int:
        number_str=str(num)
        number_str=number_str.replace("6","9",1)
        return int(number_str)