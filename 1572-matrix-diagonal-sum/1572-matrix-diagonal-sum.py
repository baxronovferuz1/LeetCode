class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or i+j==len(mat)-1:
                    s+=mat[i][j]
        return s
    # def diagonalSum(self, mat: List[List[int]]) -> int:
    #     x=mat[0]
    #     y=mat[1]
    #     z=mat[2]
    #     total=x[0]+x[-1]+y[1]+z[0]+z[-1]
    #     return total
#         top_under=[]
#         middle=[]
#         for a in mat:
#             if a[0] and a[-1]:
#                 some=top_under.append(a)
#             else:
#                 wip=middle.append(a)
            
        