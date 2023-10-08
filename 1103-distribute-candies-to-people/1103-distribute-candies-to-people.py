class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        arr = [0]*num_people
        n = 1
        while candies > 0:
            arr[(n-1)%num_people] += n if candies >= n else candies
            candies -= n
            n += 1
        return arr
        