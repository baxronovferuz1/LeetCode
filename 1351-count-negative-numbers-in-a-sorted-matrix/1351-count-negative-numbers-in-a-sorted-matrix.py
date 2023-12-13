class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative_number=0
        for i in grid:
            for a in i:
                if a<0:
                    negative_number+=1
        return negative_number
        